# Action Theory as a Pure Functional Universe

## A proposed purity architecture for an action-fundamental ontology

**Status:** Research proposal / speculative foundations

**Repository:** `lucianmarin/action-theory`

**Date:** 2026-08-19

---

## Abstract

This paper proposes a substantial refinement of Action Theory: the fundamental universe should be modeled as a **pure functional calculus of actions**, rather than primarily as a graph of weighted transitions. In this formulation, an elementary action is a pure transformation from one value domain to another. Histories are immutable compositions of previous function calls. States are observational equivalence classes of histories. Matter and energy are not primitives and are not mutable substances; they are **pure, immutable data structures derived from histories**.

The proposal has a strict architectural consequence. The fundamental layer must contain only pure values, pure actions, composition, identity, admissibility, and observational equivalence. Measurement, interaction with an observer, stochastic sampling, and other side effects must be represented explicitly as an effect layer rather than hidden in the core. This makes the theory analogous to a purely functional programming language while preserving its physics ambition: the universe is not a mutable machine containing objects, but a persistent evaluation history whose stable patterns are interpreted as objects, matter, energy, geometry, and time.

The paper defines a candidate Action Calculus, gives a typed functional formulation of histories, proposes algebraic data structures for emergent matter and energy, distinguishes derivation from interpretation, describes the required changes to the current CFR model, and identifies falsifiable mathematical and physical milestones. The central research hypothesis is:

\[
\boxed{
\text{pure action} \rightarrow \text{history} \rightarrow \text{derived data} \rightarrow \text{observable physics}
}
\]

with no primitive matter, energy, spacetime, or mutable state.

This is not a claim that the proposed construction has already recovered known physics. It is a specification for what a successful Action Theory would have to become in order to make its action-first ontology mathematically coherent and genuinely more fundamental than conventional formulations that start from spacetime, fields, particles, or an already-defined action functional.

---

## 1. Motivation

The current Action Theory repository states its primitive as an algebra/network of elementary actions and their composition rule, with the hierarchy

\[
\text{action}\rightarrow\text{history}\rightarrow\text{state}\rightarrow\text{stable object/matter}.
\]

It also defines admissible continuations \(N(h)\), freedom, Roadblocks, and a proposed freedom geometry. The physics layer remains explicitly speculative. [Action Theory repository, README](https://github.com/lucianmarin/action-theory)

The current minimal implementation, M1, is a finite weighted action graph with path composition, complex weights, path enumeration, interventions, and gauge-style rephasing. The implementation itself already distinguishes some assumptions from derived behavior, but it remains graph-centric and uses finite path enumeration as the computational representation of future possibilities. [M1 implementation](https://github.com/lucianmarin/action-theory/blob/main/models/model_m1.py)

This paper proposes a stricter foundation.

The central architectural principle is:

> **The universe should behave like a pure functional program whose execution history is reality, while matter and energy are immutable data structures obtained by evaluating or summarizing that history.**

This does not mean that the universe literally runs on a computer. The analogy is structural. The desired mathematical properties are those associated with pure functional computation: referential transparency, immutability, compositionality, explicit effects, and substitution by equivalence.

The advantage of the analogy is that it supplies a mature language for reasoning about the proposed ontology without introducing physical primitives prematurely.

---

## 2. Core Thesis

The proposed ontology is:

\[
\boxed{
\mathcal U=(\mathcal V,\mathcal A,\circ,\mathbf{id},\mathcal C)
}
\]

where:

- \(\mathcal V\) is the collection of values;
- \(\mathcal A\) is the collection of pure actions;
- \(\circ\) is composition;
- \(\mathbf{id}\) is identity;
- \(\mathcal C\) is the admissibility/type/constraint structure.

An action is a pure function between value domains:

\[
 a:A\rightarrow B.
\]

A history is a composition of actions:

\[
 h=a_n\circ\dots\circ a_2\circ a_1.
\]

If \(x\in A\), then:

\[
 h(x)=a_n(\dots a_2(a_1(x))\dots).
\]

There is no primitive mutable state. Every new state is a new immutable value produced by evaluating another pure function.

Matter and energy are not additional primitive entities. They are derived data:

\[
 M(h)=\operatorname{MatterView}(h),
\]

\[
 E(h)=\operatorname{EnergyView}(h).
\]

The decisive constraint is that these functions depend only on the relevant history and its invariants. They cannot secretly read or modify an external state.

---

## 3. Why Purity Matters

### 3.1 Referential transparency

A pure action must be substitutable by its result. If

\[
 a(x)=y,
\]

then replacing the expression \(a(x)\) by \(y\) cannot alter any other behavior.

In programming-language terms this is referential transparency. In Action Theory, it becomes an ontological rule:

> A fundamental action has no hidden side effect outside the value it returns.

This rule prevents the theory from smuggling in unexplained mutable substances, hidden clocks, external storage, or observer-dependent mutations.

### 3.2 Immutability

A history is never edited. A new history extends an old history:

\[
 h' = a\circ h.
\]

The old \(h\) remains a valid value.

This is directly analogous to persistent data structures in functional programming: new versions share conceptual ancestry without mutating previous versions.

### 3.3 Composition

Composition is the fundamental operation:

\[
(c\circ b)\circ a=c\circ(b\circ a).
\]

The action algebra therefore has a natural categorical interpretation: actions are morphisms and domains/codomains are objects. The minimum structure is a category, not a directed graph with mutable edge state.

### 3.4 Explicit effects

Observation, measurement, random sampling, intervention, irreversible export, and communication to an external environment are effects. They should not contaminate the pure core.

A pure core can therefore be written schematically as

\[
A\xrightarrow{f}B
\]

while an observational effect has a distinct shape such as

\[
A\xrightarrow{f}B\;!\;\mathsf{Measure}.
\]

The exact effect formalism is open; the principle is not: **effects must be explicit**.

This distinction is essential if Action Theory is to claim that reality is intrinsically action-first rather than observer-first.

---

## 4. The Action Calculus

### 4.1 Primitive values

The theory should contain a small set of primitive value constructors sufficient to express action composition without presupposing physical objects.

A minimal abstract syntax is:

```text
Value A

Action a : A -> B

History h = Empty | Step(h, a)
```

The primitive identity action is:

\[
\mathbf{id}_A:A\rightarrow A
\]

with

\[
\mathbf{id}_A(x)=x.
\]

### 4.2 Action composition

For

\[
a:A\rightarrow B,
\qquad
b:B\rightarrow C,
\]

composition gives

\[
 b\circ a:A\rightarrow C.
\]

The typing condition is important. If the codomain of \(a\) does not match the domain expected by \(b\), the composition is not admissible.

This makes type structure a candidate physical notion of constraint.

### 4.3 Algebraic data types

Rather than representing all things as arbitrary mutable records, the theory should prefer algebraic data types whose constructors are themselves pure values.

A schematic representation is:

```haskell
data Value
  = Unit
  | Product Value Value
  | Sum Value Value
  | Atom AtomId
  | Structured Constructor [Value]
```

This syntax is illustrative rather than normative. The physics should ultimately determine which constructors are fundamental and which are derived.

### 4.4 Histories as persistent values

A history can be represented as an immutable sequence or tree of actions:

```haskell
data History a
  = Initial a
  | Extend (History b) (Action b a)
```

The important property is semantic, not representational:

\[
\operatorname{eval}(a\circ h,x)=a(\operatorname{eval}(h,x)).
\]

History is therefore not a mutable log recording what happened to an independent universe. History **is** the structured record of the universe's prior evaluations.

---

## 5. A Stronger Definition of State

The current framework defines a state through equivalence of future possibilities:

\[
h_1\sim h_2\iff N(h_1)\cong N(h_2).
\]

This should become the central semantic notion of the functional formulation.

Define observational equivalence by:

\[
h_1\approx h_2
\iff
\forall k\in\mathcal K,
\operatorname{Obs}(k\circ h_1)=\operatorname{Obs}(k\circ h_2),
\]

where \(\mathcal K\) is the family of admissible future contexts.

Then a state is the equivalence class

\[
[h]=\{g:g\approx h\}.
\]

This has two consequences.

First, state is not stored independently from history. State is **derived from the behavior of history under all relevant continuations**.

Second, two histories that differ internally but have the same observable future semantics represent the same effective state.

This closely parallels observational equivalence in programming-language semantics and gives a more precise mathematical foundation for the existing CFR intuition.

---

## 6. Constraints Become Typing, Predicates, and Capability Rules

The existing framework defines

\[
N(h)=\{\alpha:\alpha\circ h\text{ is physically admissible}\}.
\]

In the functional formulation, admissibility should have several layers.

### 6.1 Type admissibility

If

\[
a:A\rightarrow B
\]

then it can consume only values of type \(A\). This is the strongest form of structural constraint.

### 6.2 Predicate admissibility

A predicate can constrain values:

\[
C:A\rightarrow\{\mathrm{true},\mathrm{false}\}.
\]

Then

\[
\operatorname{admissible}(a,x)\iff C(a(x)).
\]

### 6.3 Capability admissibility

A future may also be unavailable because a required capability is absent. This should be modeled explicitly instead of being hidden in mutable global configuration.

### 6.4 Roadblocks

A Roadblock becomes an empty continuation value:

\[
\operatorname{Cont}(h)=\varnothing.
\]

The functional representation should ideally use an explicit empty type or option-like constructor:

```haskell
data Continuation a
  = Open [Action a]
  | Roadblock
```

The exact representation is provisional; the semantic requirement is that a Roadblock be a first-class value denoting the absence of admissible continuation rather than an exception produced by an external runtime.

---

## 7. Freedom in a Functional Universe

The existing framework proposes

\[
F(h)=\dim N(h).
\]

That expression should be retained only after \(N(h)\) has been given a genuine mathematical structure. A raw set of functions has cardinality but not necessarily a vector-space dimension.

A stricter hierarchy is:

\[
\operatorname{Cont}(h)\rightarrow\text{algebraic structure}\rightarrow F(h).
\]

Possible choices include:

1. cardinality for finite discrete continuation sets;
2. rank of a representation of continuation functions;
3. vector-space dimension when amplitudes provide linear structure;
4. manifold dimension when a smooth continuation geometry is derived.

Only the fourth naturally supports the current proposal

\[
V_F=\sqrt{|\det G|}.
\]

Therefore the freedom geometry should not be assumed at M0. It should emerge after the continuation space acquires enough structure to define a metric or Gram form.

---

## 8. Matter as Pure Derived Data

The key ontological change in this paper is:

\[
\boxed{\text{Matter is data, not substance.}}
\]

A matter object is a stable data representation of a history equivalence class.

Define a canonicalization function:

\[
\operatorname{canon}_M:[h]\rightarrow M.
\]

Then

\[
M(h)=\operatorname{canon}_M([h]).
\]

A matter value must be immutable. Its apparent persistence comes from the fact that successive histories map into equivalent or slowly changing matter representations.

### 8.1 Stable patterns

Suppose

\[
 h_0\rightarrow h_1\rightarrow h_2\rightarrow\cdots
\]

and a coarse-graining map \(M\) satisfies

\[
M(h_i)\cong M(h_{i+1})
\]

for a long interval. Then the theory recognizes a persistent object.

Matter is therefore not an entity that persists while undergoing actions. It is the **stable pattern in the sequence of action histories**.

### 8.2 Matter as an algebraic data type

A future implementation could expose a derived type such as:

```haskell
data Matter = Matter
  { identity    :: CanonicalPattern
  , invariants  :: InvariantSet
  , support     :: HistoryRegion
  , stability   :: StabilityMeasure
  }
```

This is not a claim about the Standard Model particle ontology. It is a software-semantic representation of the proposed ontological relation.

The physics challenge is to demonstrate that familiar particles and composite matter arise as particular stable equivalence classes and that their observed quantum numbers, interactions, and masses are recovered rather than manually inserted.

---

## 9. Energy as Pure Derived Data

The repository already states that energy is not fundamental but an emergent conserved invariant associated with emergent time-translation symmetry. [Action Theory README](https://github.com/lucianmarin/action-theory)

The functional formulation makes this precise by treating energy as a data structure derived from history.

Let

\[
\operatorname{Energy}:\mathcal H\rightarrow\mathcal E
\]

map histories to an immutable energy value.

The core requirement is:

\[
E(h)=E(h')
\]

whenever the histories differ only by an admissible symmetry that represents translation along the emergent temporal direction.

### 9.1 Energy is not \(S/t\)

The standard classical statement is not generally

\[
E=S/t.
\]

The more fundamental Hamilton–Jacobi relation is that, in an appropriate formulation,

\[
E=-\frac{\partial S}{\partial t}.
\]

For Action Theory the research target should be stronger: derive the temporal parameter and the relevant action functional before defining energy.

Thus the target architecture is:

\[
\text{history}
\rightarrow
\text{emergent temporal ordering}
\rightarrow
\text{action measure}
\rightarrow
\text{energy invariant}.
\]

### 9.2 Energy as a persistent value

A possible derived structure is:

```haskell
data Energy = Energy
  { conservedQuantity :: ScalarInvariant
  , generator         :: TimeGenerator
  , provenance        :: HistoryReference
  , uncertainty       :: Maybe Measure
  }
```

The provenance field is optional at the mathematical level, but conceptually important: energy is always traceable to a history and its invariance properties.

The value must never mutate. If a later history has a different energy observable, it is a new value:

\[
E(h')\neq E(h)
\]

rather than a mutation of an energy object.

### 9.3 Energy conservation

The ambitious derivation is:

\[
\text{symmetry of pure action composition}
\Rightarrow
\text{conserved functional on histories}
\Rightarrow
E.
\]

In conventional physics, Noether's theorem connects continuous symmetries and conserved quantities. Action Theory should seek an analogous theorem on its action calculus rather than simply postulate an energy value.

---

## 10. Energy and Matter as Derived Data Structures

The central dataflow becomes:

```text
primitive actions
      |
      v
   histories
      |
      +-------------------+
      |                   |
      v                   v
 matter projection   energy projection
      |                   |
      v                   v
 immutable Matter     immutable Energy
```

Mathematically:

\[
 h
 \xrightarrow{\operatorname{MatterView}}M(h)
\]

and

\[
 h
 \xrightarrow{\operatorname{EnergyView}}E(h).
\]

Neither \(M\) nor \(E\) is primitive.

This means the same history can support multiple legitimate derived views:

\[
\operatorname{Mass}(h),
\operatorname{Charge}(h),
\operatorname{Momentum}(h),
\operatorname{Energy}(h),
\operatorname{Position}(h),
\operatorname{Entropy}(h),
\dots
\]

subject to the future derivation of each observable from the common history semantics.

The important restriction is that these quantities cannot become hidden state variables inside the core calculus.

---

## 11. Function Calls as the Fundamental Events

The phrase "function call" must be used carefully. In a physical ontology it is not assumed that there is an external computer executing a program. Instead, the analogy identifies a mathematical role:

- an action is a callable transformation;
- a history is a persistent trace of compositions;
- a result is a value;
- a stable pattern in many evaluations is a derived object;
- an invariant over histories is a derived physical quantity.

The universe can therefore be represented semantically as an immutable expression:

\[
H = a_7(a_6(a_5(a_4(a_3(a_2(a_1(x))))))).
\]

Matter and energy are analyses of this expression/history, not additional objects sitting beside it.

This is the strongest version of the "universe as a functional program" analogy.

---

## 12. Superposition and Complex Amplitudes

The current M1 assigns complex amplitudes to actions and uses multiplicative composition and path sums. [M1 implementation](https://github.com/lucianmarin/action-theory/blob/main/models/model_m1.py)

The purity architecture should retain the possibility of complex-valued representations but should not hard-code them into the primitive layer.

Introduce an optional representation functor or homomorphism:

\[
Z:\mathcal A\rightarrow\mathbb C
\]

satisfying

\[
Z(b\circ a)=Z(b)Z(a).
\]

If alternative histories can be added, require a compatible additive representation:

\[
Z(a+b)=Z(a)+Z(b).
\]

Only after those algebraic structures are established should the theory investigate whether

\[
Z(h)=e^{iS(h)/\hbar}
\]

emerges as a natural representation.

This reverses the explanatory direction from:

\[
S\rightarrow e^{iS/\hbar}
\]

toward the more fundamental target:

\[
\text{composition representation}ightarrow e^{iS/\hbar}.
\]

The latter would be more significant scientifically because it would explain why the standard action phase is the correct representation rather than merely assuming it.

---

## 13. Observation as an Effect

A pure functional universe cannot contain an implicit observer that mutates the world. Measurement must therefore be an explicit function with an effect type.

Conceptually:

```haskell
type PureAction a b = a -> b

type Observation a r = a -> (r, ObservationTrace)
```

The actual implementation should use a mathematically appropriate effect system rather than this informal tuple if the theory develops beyond the prototype stage.

This distinction gives three levels:

\[
\text{pure action}
\rightarrow
\text{derived value}
\rightarrow
\text{observable effect}.
\]

A measured value is therefore not necessarily identical to the underlying derived data structure. This preserves room for quantum measurement and epistemic limitations without making measurement a primitive alteration of reality.

---

## 14. Time as Evaluation Order

If spacetime is not primitive, the theory should not begin with a global clock.

Instead define a causal relation:

\[
a\prec b
\]

when the output domain of \(a\) is required as input to \(b\).

The transitive closure of composition induces a partial order on events/history segments.

A temporal parameter may then be introduced as a representation of sufficiently regular chains in this partial order:

\[
\tau:H\rightarrow\mathbb R.
\]

A successful continuum limit would need to demonstrate that such a parameter reproduces ordinary time while preserving the pure core.

This is stronger than merely declaring that "time emerges from causal ordering." It specifies what has to be constructed and tested.

---

## 15. Space as Independence Geometry

Pure functions naturally express dependency. Space should therefore initially be represented not by coordinates but by **independence and separability relations**.

Two action substructures \(A\) and \(B\) are independent when their compositions factor appropriately:

\[
\mathcal A_{AB}\cong\mathcal A_A\otimes\mathcal A_B.
\]

The space-like structure can then be sought in the geometry of families of mutually compatible independent action directions.

Only later should a metric be introduced.

The existing repository already proposes that space emerge from the geometry of mutually independent action directions and that time emerge from causal ordering. [Action Theory README](https://github.com/lucianmarin/action-theory)

The purity reformulation therefore preserves the direction but removes the temptation to insert a metric too early.

---

## 16. Matter as a Fold Over History

A functional-language analogy suggests a useful formal mechanism: **folding** a history into a derived summary.

Suppose a history is

\[
h=[a_1,a_2,\dots,a_n].
\]

A derived matter representation can be generated by

\[
M(h)=\operatorname{fold}_M(m_0,a_1,\dots,a_n).
\]

Likewise:

\[
E(h)=\operatorname{fold}_E(e_0,a_1,\dots,a_n).
\]

These folds do not mutate \(m_0\) or \(e_0\). They generate new immutable values.

However, a pure fold alone is not enough. The research must show that the resulting summaries are invariant under changes of history that should represent the same physical state.

Thus the real requirement is:

\[
h_1\approx h_2
\Rightarrow
M(h_1)=M(h_2)
\]

and, for frame-appropriate energy,

\[
h_1\approx h_2
\Rightarrow
E(h_1)=E(h_2).
\]

---

## 17. Matter Is Not Just a Snapshot

A dangerous simplification would be to define matter as an instantaneous snapshot of some computed array.

The proposal instead requires **history-derived persistence**.

Let \(P\) be a candidate pattern detector:

\[
P(h)=\{0,1\}.
\]

A stable matter pattern occurs when:

\[
P(h_i)=1
\]

for a sufficiently large set of successive or causally related histories and when perturbations do not immediately destroy the equivalence class.

This introduces a stability functional

\[
\Sigma(P,h)
\]

whose exact form must be derived.

Particles, bound states, and macroscopic objects would then be candidate fixed points or long-lived attractors of the history semantics rather than primitive entities.

---

## 18. Energy Is Not a Second Substance

The pure-data thesis requires a strict ban on the following move:

> "Energy is a derived quantity, therefore attach an energy field to every primitive action."

That would simply reintroduce energy as a disguised primitive.

Instead, primitive actions carry only whatever structure is necessary for the fundamental calculus. Energy appears only after a history has sufficient symmetry and regularity to support an energy functional.

The dependency should be one-way:

\[
\text{actions}
\rightarrow
\text{histories}
\rightarrow
\text{symmetries/invariants}
\rightarrow
E.
\]

Not:

\[
\text{actions}
+E
\rightarrow
\text{histories}.
\]

The same rule applies to matter, mass, momentum, position, charge, entropy, and spacetime geometry.

---

## 19. A Candidate Type System for Physics

A successful Action Theory language could use typed actions to make impossible compositions structurally unrepresentable.

For example:

```haskell
createAtom      :: Seed -> AtomState
emitPhoton      :: ExcitedAtom -> (AtomState, Photon)
absorbPhoton    :: (AtomState, Photon) -> GroundState
```

A composition such as

```haskell
emitPhoton . emitPhoton
```

would be invalid unless the output type of the first action matches the input type of the second.

In the physical interpretation, such a type mismatch is not a programming error accidentally added by the model. It represents a candidate form of **structural physical impossibility**.

This should be called **type-level constraint**, while dynamical restrictions should remain predicate-level constraints.

The theory should test whether known conservation and selection rules can emerge from typing and composition rather than being separately listed.

---

## 20. Conservation Laws as Pure Invariants

Let

\[
I:\mathcal H\rightarrow V
\]

be an invariant over histories.

A conservation law is then:

\[
I(h)=I(a\circ h)
\]

for all admissible actions \(a\) in a specified symmetry class.

Energy would be one candidate invariant. Others might include momentum, charge, particle-number-like quantum numbers, or topological invariants.

The strongest goal is therefore not to build a database of physical constants into actions, but to derive a family of invariants from the algebraic symmetries of the calculus.

This is the functional analogue of asking which quantities survive program transformations that preserve semantics.

---

## 21. Rewriting and Evaluation

A pure functional language admits multiple evaluation strategies when semantics are preserved. Action Theory should exploit this.

Two histories may have different internal decompositions:

\[
h=(c\circ b)\circ a
\]

and

\[
h'=c\circ(b\circ a).
\]

Associativity requires semantic equality:

\[
h\equiv h'.
\]

More generally, a rewrite system can define when histories are interchangeable without changing their denotation.

This produces an important research program:

> **Physical state should correspond to equivalence under semantics-preserving history rewrites.**

Matter can then be seen as a stable normal form or invariant quotient of histories.

Energy can be a conserved annotation/invariant of the same quotient.

---

## 22. Lazy Evaluation and the Future

There is an especially useful analogy with lazy evaluation.

A history need not enumerate every possible future in advance. It can denote a space of possible continuations lazily.

Instead of constructing

\[
N(h)=\{\alpha_1,\alpha_2,\ldots\}
\]

as a finite graph, represent continuation as a generator:

```haskell
continuations :: History a -> Stream (Action a)
```

The mathematical object can be infinite even if a particular observation requests only a finite portion.

This is potentially important for an Action Theory that does not yet know whether the universe is finite or infinite.

The repository currently leaves that question unresolved. [Action Theory README](https://github.com/lucianmarin/action-theory)

The functional formulation lets the theory remain agnostic without forcing a finite graph into the ontology.

---

## 23. Concurrency and Independent Actions

Pure functional composition naturally handles sequencing. Physics also needs independent operations.

Introduce a product/combinator for independent actions:

\[
(a\otimes b)(x,y)=(a(x),b(y)).
\]

Then the fundamental calculus potentially has both:

\[
\circ \quad \text{(sequential composition)}
\]

and

\[
\otimes \quad \text{(independent composition)}.
\]

This is a major improvement over a simple graph because it gives the theory a natural place to represent separability, parallel composition, and entanglement.

An entangled structure is then not merely two paths that happen to be correlated; it is a failure of a proposed factorization into independent action components.

That matches the current CFR intuition while giving it a more explicit algebraic form.

---

## 24. Entanglement as Failure of Functional Factorization

Define factorization when a joint action system can be represented as

\[
\mathcal A_{AB}\cong\mathcal A_A\otimes\mathcal A_B.
\]

If no such factorization exists under the allowed semantics, the joint structure is nonfactorizable.

The proposal is:

\[
\boxed{
\text{entanglement}=
\text{nonfactorizability of joint action semantics}
}
\]

This is a functional analogue of compositional independence.

The theory must still recover the quantitative quantum formalism and the no-signalling constraints. Nonfactorizability alone is not enough.

---

## 25. Gauge Symmetry as Representation Redundancy

The current M1 includes a local \(U(1)\)-style rephasing and labels gauge structure as an assumption rather than a derivation. [M1 implementation](https://github.com/lucianmarin/action-theory/blob/main/models/model_m1.py)

Under the purity architecture, a gauge transformation should be a semantics-preserving transformation of an action representation:

\[
R\rightarrow R'
\]

such that

\[
\operatorname{Obs}(R,h)=\operatorname{Obs}(R',h)
\]

for all admissible observations.

The research target is therefore:

\[
\boxed{
\text{gauge symmetry}=
\text{redundancy in the representation of the same pure action semantics}
}
\]

This is cleaner than attaching gauge freedom as an arbitrary edge-label symmetry.

---

## 26. The Runtime Is Not the Universe

A crucial methodological rule is needed.

The software implementation must never be confused with the ontology.

A Python class such as:

```python
class Action:
    ...
```

is only a representation of the mathematical object.

The desired semantics should be language-independent:

\[
\text{mathematical pure action}
\neq
\text{Python object}
\neq
\text{graph edge}.
\]

The implementation should be a reference interpreter and experiment platform.

This prevents implementation details such as dictionary mutation, object identity, floating-point arithmetic, and list order from accidentally becoming physics.

---

## 27. Required Changes to the Existing Action Theory Architecture

The current repository is organized around a README, a research handoff, an M1 model, and notes. [Action Theory repository](https://github.com/lucianmarin/action-theory)

The following changes are recommended.

### 27.1 Introduce M0: the Pure Action Calculus

Create a new model whose only concerns are:

- values;
- typed pure actions;
- identity;
- composition;
- product/parallel composition;
- constraints;
- histories;
- observational equivalence;
- continuation generation;
- Roadblocks.

M0 must contain **no spacetime, particles, energy, matter, complex amplitudes, gauge fields, or numerical physics constants**.

### 27.2 Demote the graph

The graph should become one concrete representation of an action calculus, not the ontology itself.

A graph visualization should be generated from actions and their types where useful.

### 27.3 Remove mutation from model APIs

Every transformation should return a new value.

Bad semantic pattern:

```text
model.disable(x)
model.add_weight(y)
```

Preferred pattern:

```text
restricted = restrict(model, constraint)
weighted   = assignRepresentation(model, representation)
```

### 27.4 Separate the type layer from the physical layer

The type system should represent structural composability before introducing physical interpretations.

### 27.5 Add explicit effect types

Observation, measurement, sampling, and intervention should be effectful operations outside the pure core.

### 27.6 Replace path enumeration with continuation semantics

Finite-depth path enumeration may remain as an implementation technique, but the theory must define the underlying continuation object independently of that truncation.

### 27.7 Derive matter and energy through projection functions

Introduce conceptual APIs:

```text
MatterView   : History -> Matter
EnergyView   : History -> Energy
StateView    : History -> State
GeometryView : History -> Geometry
```

Each must be a pure function.

### 27.8 Introduce a canonical equivalence layer

Two histories with the same relevant semantics should collapse to the same state representation. Canonicalization should never modify the original histories.

### 27.9 Treat amplitudes as a representation layer

Complex amplitudes should belong to M1 or later, not M0.

### 27.10 Make the physics derivations downstream of the calculus

The research order should become:

\[
M0\rightarrow M1\rightarrow M2\rightarrow\dots
\]

where each level inherits the pure semantics of the previous level and adds structure only with an explicit derivation.

---

## 28. Proposed Repository Layout

A proposed structure is:

```text
action-theory/
├── README.md
├── docs/
│   ├── research-purity.md
│   ├── research-handoff.md
│   ├── action-calculus.md
│   ├── semantics.md
│   └── epistemic-status.md
│
├── core/
│   ├── values.py
│   ├── actions.py
│   ├── compose.py
│   ├── products.py
│   ├── constraints.py
│   ├── histories.py
│   ├── equivalence.py
│   └── effects.py
│
├── models/
│   ├── model_m0_pure.py
│   ├── model_m1_amplitudes.py
│   ├── model_m2_geometry.py
│   └── model_m3_physics.py
│
├── derived/
│   ├── state.py
│   ├── matter.py
│   ├── energy.py
│   ├── momentum.py
│   └── geometry.py
│
└── tests/
    ├── test_identity.py
    ├── test_associativity.py
    ├── test_purity.py
    ├── test_equivalence.py
    ├── test_constraints.py
    ├── test_roadblocks.py
    ├── test_product_composition.py
    ├── test_matter_derivation.py
    └── test_energy_derivation.py
```

The names are recommendations, not mandatory implementation details.

---

## 29. M0: Minimal Axioms

The following axioms should be treated as the first formal target.

### Axiom 1 — Purity

Every primitive action is a total or explicitly typed partial function with no hidden state mutation.

### Axiom 2 — Identity

Every admissible value domain has an identity action.

### Axiom 3 — Associative composition

\[
(c\circ b)\circ a=c\circ(b\circ a).
\]

### Axiom 4 — Type compatibility

Only actions with compatible domains/codomains compose.

### Axiom 5 — Persistent history

Extending a history never mutates its prefix.

### Axiom 6 — Explicit admissibility

All restrictions on composition are represented by types, predicates, capabilities, or explicit constraints.

### Axiom 7 — Observational equivalence

Histories producing identical behavior for all allowed future contexts are equivalent.

### Axiom 8 — Derived objecthood

Objects are equivalence classes or stable patterns of histories, not primitives.

### Axiom 9 — Derived physical quantities

Matter, energy, geometry, momentum, and related observables are pure functions of history and its equivalence/invariant structure.

### Axiom 10 — No hidden effects

Measurement, observation, sampling, and intervention are effectful extensions of the pure calculus and never silently modify its semantics.

---

## 30. Proposed Reference Semantics

A reference semantic interpreter should expose only pure operations:

```text
compose      : Action B C -> Action A B -> Action A C
identity     : Action A A
apply        : Action A B -> A -> B
extend       : History A -> Action A B -> History B
continue     : History A -> Continuations A
stateView    : History A -> State
matterView   : History A -> Matter
energyView   : History A -> Energy
```

The implementation language may be Python, Haskell, OCaml, Rust, or another language. The semantic contract is what matters.

The Python prototype should use immutable dataclasses or equivalent persistent representations and should forbid mutation through code review and tests.

---

## 31. Purity Tests

The new test suite should contain explicit purity properties.

### Test 1: Repeatability

For pure \(f\):

\[
f(x)=f(x)
\]

across repeated evaluation.

### Test 2: No mutation

Applying an action does not change the input value or history.

### Test 3: Composition

\[
\operatorname{apply}(b\circ a,x)
=
\operatorname{apply}(b,\operatorname{apply}(a,x)).
\]

### Test 4: Identity

\[
\operatorname{apply}(\mathbf{id},x)=x.
\]

### Test 5: Equivalence stability

If \(h_1\approx h_2\), then derived state is identical:

\[
\operatorname{State}(h_1)=\operatorname{State}(h_2).
\]

### Test 6: Derived-data determinism

\[
\operatorname{Energy}(h)=\operatorname{Energy}(h)
\]

independent of evaluation order or storage identity.

### Test 7: Effect isolation

Observation cannot alter the denotation of a pure history.

These tests are prerequisites for calling M0 a pure action calculus.

---

## 32. From Pure Calculus to Physics

Once M0 exists, physical structure can be introduced in stages.

### M1 — Linear/complex representation

Ask whether the pure action algebra admits a natural complex or linear representation.

Target questions:

- Does complex phase emerge?
- Does interference arise?
- Can a norm emerge?
- Can unitary evolution be derived?
- Can a Born-type probability rule be derived?

### M2 — Continuation geometry

Construct the mathematical structure needed for

\[
G_{AB}
\]

and determine whether

\[
V_F=\sqrt{|\det G|}
\]

is invariant and physically meaningful.

### M3 — Emergent spacetime

Seek causal order, locality, topology, dimensionality, and a Lorentzian signature from the pure calculus.

### M4 — Derived matter and energy

Demonstrate stable matter patterns and derive energy as an invariant of the emergent temporal symmetry.

### M5 — Gravity and quantum fields

Only after the previous layers work should the theory attempt the Einstein and Standard Model limits.

This is a much stricter research sequence than simultaneously asserting all layers.

---

## 33. What Must Not Be Assumed in M0

M0 must explicitly prohibit the following primitive assumptions:

- time as a real-valued global variable;
- space as a coordinate manifold;
- particles as primitive objects;
- mass as a primitive scalar;
- energy as a primitive scalar;
- momentum as a primitive vector;
- fields as primitive functions on spacetime;
- metric tensor as primitive data;
- complex amplitudes as primitive physical structure;
- Born probabilities;
- gauge groups;
- Planck's constant;
- the speed of light;
- a Hamiltonian;
- the Lagrangian action functional \(\int L\,dt\).

Those may all appear later, but their presence must carry an epistemic label: assumed, derived, effective, or predicted.

This matters because a theory that begins by assigning energy, momentum, spacetime, or particles to primitive actions has not demonstrated that they emerge.

---

## 34. Relation to the Conventional Action Functional

The conventional classical action is

\[
S[\gamma]=\int L\,dt.
\]

Action Theory should treat this as a **derived continuum representation** rather than its primitive definition.

The target derivation is:

\[
\text{discrete/pure action calculus}
\rightarrow
\text{continuum history space}
\rightarrow
\text{action measure }S[\gamma]
\rightarrow
\text{Lagrangian density }L.
\]

A successful derivation would answer the foundational question: why is the world representable by a variational action in the first place?

A failure to derive this relation would limit Action Theory to an alternative ontology or interpretation rather than a deeper physical theory.

---

## 35. Energy Without Primitive Time

A successful theory should eventually produce an emergent temporal generator

\[
T
\]

or vector field/operator associated with causal progression.

Then define an energy functional through the history-action relation, schematically:

\[
E(h)=-T[S](h).
\]

The sign and exact mathematical form are provisional until the action and temporal geometry are derived.

The research target is not the equation itself but the dependency order:

\[
\boxed{
\text{composition}
\rightarrow
\text{causal order}
\rightarrow
T
\rightarrow
S
\rightarrow
E
}
\]

If a derivation instead requires \(t\), \(L\), or \(H\) as input, then the purported emergence has not occurred.

---

## 36. Energy as a History Annotation

Once energy is derived, it can be represented as a pure annotation of a history:

\[
(h,E(h)).
\]

This annotation is not causally prior to the history.

The direction of explanation is:

\[
 h\Rightarrow E(h),
\]

not

\[
 E\Rightarrow h.
\]

This distinction permits multiple derived observables from the same history:

\[
 h\Rightarrow
\begin{cases}
E(h)\\
P(h)\\
M(h)\\
Q(h)\\
G(h)
\end{cases}
\]

This is analogous to computing several views over one immutable persistent data structure.

---

## 37. Matter as a History Quotient

Matter should not be the value of a single history node. It should be the quotient of many histories that exhibit the same stable behavior.

Let \(\sim_M\) be an equivalence relation induced by matter-relevant observations. Then:

\[
\operatorname{MatterClass}(h)=[h]_{\sim_M}.
\]

A canonical data structure can then represent the quotient class.

This provides a direct route from history semantics to apparent object permanence:

\[
\text{many histories}\rightarrow\text{one stable matter pattern}.
\]

The object is therefore a compressed semantic summary of process, not an independently existing thing.

---

## 38. Complexity and Compression

Pure functional implementations invite an additional hypothesis: stable matter may correspond to histories that admit highly compressed descriptions without losing predictive power.

This suggests a possible research quantity:

\[
K(h)=\text{minimum description complexity of the state-relevant semantics of }h.
\]

Matter-like objects may occupy regions in which a compact invariant description remains valid across many future histories.

This is deliberately speculative. It should not be confused with a claim that Kolmogorov complexity is itself the physical ontology.

Its value is methodological: stable objects should be represented by persistent summaries rather than by enumerating all of their microscopic histories.

---

## 39. Roadblocks as Type Failure vs. Semantic Failure

The pure-functional framework suggests two distinct Roadblocks.

### Structural Roadblock

No well-typed continuation exists:

\[
\operatorname{Cont}_{\mathrm{type}}(h)=\varnothing.
\]

### Semantic/Dynamical Roadblock

Well-typed continuations exist, but none satisfy the admissibility predicates:

\[
\operatorname{Cont}_{\mathrm{admissible}}(h)=\varnothing.
\]

This distinction is valuable because it separates impossible composition from dynamically forbidden composition.

A third possibility remains:

### Geometric Roadblock

The continuation space still exists, but its derived geometry becomes degenerate:

\[
\det G(h)=0.
\]

The current Action Theory repository already proposes Roadblocks in terms of both continuation closure and freedom-geometry degeneracy. [Action Theory README](https://github.com/lucianmarin/action-theory)

The pure formulation makes the distinctions operational.

---

## 40. A Functional Interpretation of Freedom

A functional program is powerful when many valid computations remain available from a given expression. That is analogous to the CFR intuition of freedom as future possibility.

For a history \(h\), define its continuation algebra:

\[
\mathcal C(h)=\{a\mid a\circ h\text{ is admissible}\}.
\]

Then freedom is not simply "number of outgoing edges." It is a property of the algebra of composable transformations.

Potentially:

\[
F(h)=\operatorname{rank}(\mathcal C(h))
\]

or, once a measure exists,

\[
F(h)=\operatorname{Vol}(\mathcal C(h)).
\]

This replaces an implementation-dependent graph statistic with a semantic property.

---

## 41. Referential Transparency as a Physical Principle

A particularly strong version of the proposal is:

> Two histories are physically indistinguishable whenever every admissible continuation returns the same observable values.

Formally:

\[
h_1\approx h_2
\Rightarrow
\forall k,\;
\operatorname{Obs}(k\circ h_1)=\operatorname{Obs}(k\circ h_2).
\]

This turns referential transparency into a physical criterion of identity.

An object is therefore not a hidden substance behind its behavior. Its identity is exhausted by the equivalence class of its future semantics.

That is a direct functional analogue of the repository's existing claim that a state is an equivalence class of histories with equivalent futures.

---

## 42. What Would Count as Success?

The purity reformulation should be judged by explicit milestones.

### Mathematical milestones

1. A complete formal definition of the pure action calculus.
2. A proof of semantic consistency of composition and identity.
3. A rigorous equivalence relation over histories.
4. A well-defined continuation object.
5. A derivation of state from observational equivalence.
6. A derivation of stable matter classes.
7. A derivation of at least one nontrivial conserved invariant identified with energy.
8. A precise continuation geometry, if the freedom-volume program is retained.

### Physical milestones

1. Recover quantum interference without assuming the conventional path-integral phase.
2. Recover a probability rule without simply inserting the Born rule.
3. Recover causal structure and a viable relativistic limit.
4. Recover known matter excitations without inserting particle species.
5. Recover an energy observable with the correct dimensions and conservation behavior.
6. Recover standard low-energy physics in the appropriate limit.
7. Produce at least one quantitative prediction that differs from standard theory.

Until these milestones are met, the framework remains a speculative foundations program.

---

## 43. Falsification Criteria

The theory should be considered unsuccessful in this formulation if any of the following occurs:

- primitive energy or matter must be inserted to reproduce the observed theory;
- the core requires hidden mutable state;
- measurement changes pure semantics without an explicit effect mechanism;
- the same history can yield different derived matter or energy values for no semantic reason;
- standard spacetime is assumed to define the primitive action calculus;
- the continuum action \(S=\int Ldt\) is simply postulated rather than derived when derivation is claimed;
- the functional encoding produces no explanatory advantage over an equivalent conventional formalism;
- the proposed physical predictions are unfalsifiable;
- the freedom geometry depends irreducibly on arbitrary implementation choices such as path-enumeration depth.

These criteria are intentionally demanding.

---

## 44. Relationship to Existing Action Theory Claims

The proposed purity architecture preserves the strongest existing CFR ideas:

\[
\text{action}\rightarrow\text{history}\rightarrow\text{state}\rightarrow\text{stable pattern}.
\]

It changes their mathematical interpretation:

| Existing CFR concept | Pure-functional reformulation |
|---|---|
| primitive action | pure typed function |
| action composition | function composition |
| history | persistent expression/call history |
| state | observational equivalence class |
| object/matter | stable derived data structure |
| energy | invariant data derived from history |
| constraint | type/predicate/capability restriction |
| freedom | structure of admissible continuation functions |
| Roadblock | empty continuation / semantic singularity |
| interference | algebraic combination of alternative pure histories |
| entanglement | failure of functional factorization |
| gauge symmetry | representation redundancy preserving semantics |
| time | derived evaluation/causal order |
| space | derived independence geometry |
| measurement | explicit effect |
| physics | invariant semantics of the action calculus |

This is not a change of vocabulary only. It changes what the theory has to prove.

---

## 45. Comparison with Conventional Functional Programming

The analogy should be made precise but not literal.

A pure functional language has:

\[
\text{values} + \text{functions} + \text{composition} + \text{types} + \text{effects}.\n\]

The proposed physical analogue is:

\[
\text{values} + \text{actions} + \text{composition} + \text{constraints} + \text{observations}.\n\]

In both cases:

- functions/actions do not mutate their arguments;
- results are immutable values;
- composite expressions are built from smaller transformations;
- equivalent expressions can be substituted;
- effects are separated from pure computation.

The analogy should stop there. The universe is not thereby proved to be a computer program, nor does the programming-language implementation itself explain the physical constants or dynamics.

---

## 46. Proposed Terminology

To avoid importing too much computer-science vocabulary directly into physics, the theory can use paired terminology.

| Functional term | Action Theory term |
|---|---|
| function | action |
| function composition | action composition |
| function argument | input value |
| return value | resulting value |
| evaluation | action realization / history extension |
| persistent data | stable derived pattern |
| pure function | pure action |
| effect | observation/intervention |
| type | composability domain |
| type error | structural incompatibility |
| lazy stream | continuation space |
| fold | history aggregation |
| memoization | derived invariant/cache representation |
| observational equivalence | physical state equivalence |

This keeps the functional analogy useful without claiming that the metaphysics is identical to software engineering.

---

## 47. The Most Important Change in the Research Philosophy

The research should stop asking:

> "How can action theory describe matter, energy, space, time, and quantum mechanics?"

and ask instead:

> "What mathematical structures must necessarily emerge from a pure algebra of composable actions, and do the resulting invariants coincide with matter, energy, geometry, and known physics?"

This changes the burden of proof from reinterpretation to derivation.

The theory should therefore maintain a strict status table:

| Statement | Required status |
|---|---|
| Pure action composition exists | axiom / definition |
| Histories are persistent values | axiom / semantics |
| States are history equivalence classes | theorem if equivalence is established |
| Matter is a stable history quotient | derived hypothesis to test |
| Energy is a history invariant | derived hypothesis to prove |
| \(S=\int Ldt\) emerges | derivation target |
| \(e^{iS/\hbar}\) emerges | derivation target |
| Born rule emerges | derivation target |
| spacetime emerges | derivation target |
| Standard Model emerges | long-term derivation target |
| new physics emerges | prediction target |

This preserves the repository's existing epistemic discipline while making it stricter.

---

## 48. A Minimal Example

Consider three pure actions:

\[
a:A\rightarrow B,
\qquad
b:B\rightarrow C,
\qquad
c:C\rightarrow D.
\]

The history is

\[
h=c\circ b\circ a.
\]

Suppose a derived matter map gives:

\[
M(h)=m.
\]

Suppose a derived energy map gives:

\[
E(h)=e.
\]

The universe does not contain separate primitive entities \(m\) and \(e\). They are views of the same history:

\[
 h
 \rightarrow
 \begin{cases}
 m\\
 e
 \end{cases}.
\]

Extend the history by \(d:D\rightarrow E\):

\[
 h'=d\circ h.
\]

The old history remains unchanged, while new derived values are computed:

\[
M(h')=m',
\qquad
E(h')=e'.
\]

If \(m'\cong m\), the matter pattern persisted.

If \(e'=e\), the relevant energy invariant was conserved.

If no admissible \(d\) exists, the continuation is a Roadblock.

This captures a large portion of CFR's intended semantics without introducing a mutable universe state.

---

## 49. A Stronger Long-Term Formulation

The eventual theory could aim for the following decomposition:

\[
\boxed{
\begin{aligned}
\textbf{Primitive:}&\quad \text{pure actions and composition}\\
\textbf{Derived:}&\quad \text{histories and equivalence classes}\\
\textbf{Stable:}&\quad \text{matter-like data structures}\\
\textbf{Invariant:}&\quad \text{energy and other conserved quantities}\\
\textbf{Geometric:}&\quad \text{space, time, metric}\\
\textbf{Observable:}&\quad \text{measurements and probabilities}\\
\textbf{Effective:}&\quad \text{QM, GR, SM limits}
\end{aligned}
}
\]

That hierarchy is stronger than the current statement that "everything is a stable, coarse-grained pattern of action" because it specifies the computational-semantic mechanism by which the patterns are obtained.

---

## 50. Research Program

The immediate implementation program should be:

### Phase A — Pure core

Build M0 and prove:

\[
\text{purity} + \text{composition} + \text{identity} + \text{equivalence}.
\]

### Phase B — Histories and continuations

Replace finite graph traversal as the ontology with lazy/persistent continuation semantics.

### Phase C — Derived state

Implement state as observational equivalence and test canonicalization.

### Phase D — Matter

Search for stable fixed points, attractors, or long-lived equivalence classes and represent them as immutable derived data.

### Phase E — Energy

Search for continuous/discrete symmetries of the history calculus and derive a conserved invariant that behaves as energy.

### Phase F — Quantum representation

Investigate complex and linear representations, interference, and probability.

### Phase G — Geometry

Construct the continuation geometry and test whether space, time, and Lorentzian structure emerge.

### Phase H — Physical limits

Recover known quantum, relativistic, and field-theoretic behavior.

### Phase I — New predictions

Only after the recovery program succeeds, derive observable deviations.

---

## 51. Open Mathematical Questions

The following questions are fundamental.

1. What is the minimal category/algebra of actions needed for all later constructions?
2. Are actions morphisms in a category, arrows in a groupoid, elements of an algebra, or something richer?
3. What is the exact mathematical structure of a continuation space?
4. Under what conditions does a history admit a canonical finite description?
5. What equivalence relation turns histories into physical states?
6. Which invariants of composition can represent energy and other conserved quantities?
7. Can an action representation naturally generate complex amplitudes?
8. Can additive and multiplicative structures coexist without being imposed ad hoc?
9. What mechanism produces a continuum limit?
10. What structures generate dimensionality and Lorentzian signature?
11. What is the exact relationship between stable history quotients and particle-like excitations?
12. Can the entire theory be formulated in a language-independent denotational semantics?

---

## 52. Open Physical Questions

1. Can energy be derived without a primitive time parameter?
2. Can mass arise as an invariant of a stable history pattern?
3. Can momentum arise from a symmetry of action translations?
4. Can charge arise from a representation symmetry?
5. Can quantum probabilities be derived rather than assumed?
6. Can locality and no-signalling emerge from compositional constraints?
7. Can entanglement emerge from nonfactorization alone?
8. Can spacetime emerge without embedding the action calculus in a pre-existing manifold?
9. Can Einstein dynamics arise as an effective law of derived geometry?
10. Can Roadblocks produce quantitatively testable corrections?
11. Does the theory reproduce the Standard Model spectrum without inserting it?
12. Does it make a prediction that distinguishes it from standard quantum field theory and general relativity?

---

## 53. Final Proposal

The central proposal of this paper is simple:

\[
\boxed{
\textbf{The universe is a pure functional calculus of actions.}
}
\]

A primitive action is a pure transformation.

A history is an immutable composition of previous actions.

A state is an equivalence class of histories with equivalent future semantics.

Matter is a stable pure data structure derived from those histories.

Energy is a pure invariant data structure derived from those histories.

Space and time are prospective derived structures over the action calculus.

Measurement is an explicit effect rather than a hidden mutation.

Physics is the study of the invariants and continuum limits of this calculus.

The resulting dependency graph is:

\[
\boxed{
\text{action}
\rightarrow
\text{composition}
\rightarrow
\text{history}
\rightarrow
\text{equivalence}
\rightarrow
\text{derived data}
\rightarrow
\text{invariants}
\rightarrow
\text{geometry}
\rightarrow
\text{effective physics}
}
\]

The strongest form of the project is therefore not "action is fundamental" in the conventional variational sense. It is:

> **All apparent things are values returned by a pure action calculus, and all persistent physical quantities are immutable invariants of the histories that produce those values.**

If this architecture can derive the conventional action functional, energy, matter, quantum amplitudes, and spacetime rather than merely rename them, it would provide the mathematical foundation that the current Action Theory program is still missing.

If it cannot, the failed derivations will still identify precisely which additional primitives are required.

That is the correct standard for the next stage of the theory.

---

## References

1. **Action Theory repository.** `lucianmarin/action-theory`, current README and project structure. https://github.com/lucianmarin/action-theory
2. **Action Theory M1 implementation.** `models/model_m1.py`. https://github.com/lucianmarin/action-theory/blob/main/models/model_m1.py
3. **Action Theory research handoff.** `docs/research-handoff.md`. https://github.com/lucianmarin/action-theory/blob/main/docs/research-handoff.md
4. Haskell 2010 Language Report, sections covering pure functional semantics and type structure. https://www.haskell.org/onlinereport/haskell2010/
5. Moggi, E. (1991). *Notions of Computation and Monads*. Information and Computation, 93(1), 55–92. https://doi.org/10.1016/0890-5401(91)90052-4
6. Wadler, P. (1992). *The Essence of Functional Programming*. Proceedings of the 19th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages. https://doi.org/10.1145/143165.143169
7. Mac Lane, S. (1998). *Categories for the Working Mathematician*. Springer.
8. Noether, E. (1918). *Invariante Variationsprobleme*. Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse.

---

## Epistemic Status of This Paper

The paper is a **research architecture and hypothesis specification**, not a proof that the universe is a functional program or that matter and energy have already been derived from action.

The following statements are proposals:

- pure action is the sole fundamental computational-like primitive;
- histories are persistent function-call structures;
- matter is a stable history-derived data structure;
- energy is a history-derived invariant/data structure;
- time and space emerge from ordering and independence;
- observation is an effect layer.

The following are implementation/design requirements of the proposal:

- no mutation in M0;
- explicit types/constraints;
- explicit effects;
- history equivalence;
- derived-value projections;
- separation of representation from ontology.

The following remain empirical/theoretical derivation targets:

- quantum amplitudes;
- Born probabilities;
- Lorentzian spacetime;
- the Standard Model;
- Einstein gravity;
- a quantitative new prediction.

The purpose of this document is therefore to make Action Theory **more falsifiable, more compositional, and more mathematically explicit**, not to imply that those unresolved results have already been achieved.
