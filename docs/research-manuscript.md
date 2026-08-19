# The Functional Universe: Action as the Sole Primitive of Physics

**A Purely Functional Foundation in which Mass, Energy, Fields, Spacetime, and Measurement Emerge from Composition**

*Author: Lucian Marin*
*Status: Speculative research program — foundational manuscript, draft 1.0*

---

## Abstract

We propose a foundational framework — **Pure Functional Dynamics (PFD)** — in which the *action* is not a property of things but the only primitive of reality, and is formalized literally as a *function* in a small, strictly defined calculus we call the **Action Calculus** ($\Lambda_{\!A}$). The universe is a single closed term $\mathcal{U}$ of this calculus; every physical fact is a fact about how $\mathcal{U}$ evaluates. The calculus is *purely functional*: actions have no side effects, no mutable state, and no hidden variables — only composition, application, abstraction, and shared deferral (laziness). From these four ingredients, plus a single discrete cost grading, we *derive* the familiar furniture of physics as theorems or forced structural correspondences: time is the partial order of reduction steps; causality is data dependence; Lorentz invariance is the Church–Rosser theorem; energy conservation is the invariance of the cost grade under reduction (a purity-based Noether theorem); mass is the cost of redirecting an action; fields are shared environments (memo tables); gauge symmetry is $\alpha$-equivalence; particles are recursion fixed points; superposition is the set of unevaluated reduction paths of a thunk; entanglement is thunk sharing; measurement is forcing. Because terms are finite syntactic objects, the quantum of action $\hbar$ is a *theorem of discreteness*, not a postulate. We then describe what a "purely functional universe" looks like phenomenologically, and extract new, falsifiable predictions — including structured deviations from unitary quantum mechanics at extreme evaluation complexity ("non-confluence noise"), an exact masslessness theorem for gauge bosons, a gravitational contribution from unforced computations ("thunk gravity" as a dark-matter candidate), and a theorem-level Margolus–Levitin bound. The mathematics is kept deliberately strict and simple: every claim is labeled **Theorem** (provable inside the calculus), **Postulate** (physical interpretation), or **Conjecture** (open).

---

## Contents

1. Introduction: Why Action, and Why Functions
2. The Action Calculus $\Lambda_{\!A}$: Syntax, Types, Reduction, Cost
3. The Physical Postulates
4. Emergence I — Time, Causality, and the Light Cone
5. Emergence II — Confluence as Relativity
6. Emergence III — Energy, Mass, and Conservation Laws
7. Emergence IV — Fields, Gauge Symmetry, and Particles
8. Quantum Phenomena from Laziness
9. Gravity as Evaluation-Cost Geometry
10. The Phenomenology of a Purely Functional Universe
11. Predictions and Falsifiability
12. Relation to Existing Science
13. Open Problems
14. Conclusion
- Appendix A: Proofs Omitted from the Main Text
- Appendix B: A Worked Micro-Universe
- References

---

## 1. Introduction: Why Action, and Why Functions

### 1.1 The inversion

Classical mechanics begins with *things* — particles with positions and masses — and defines the *action* $S = \int L\,dt$ as a functional of their trajectories. Quantum mechanics begins with *states* and *fields* and treats action as a weight $e^{iS/\hbar}$ in a sum over histories. In both frameworks, action is bookkeeping: a number assigned to entities that are taken as primary.

Yet the history of physics keeps hinting that the bookkeeping is more fundamental than the books. The principle of least action (Maupertuis, Euler, Lagrange, Hamilton) derives all of classical dynamics from a single scalar. Noether's theorem ties every conservation law to a symmetry of the action. Feynman's path integral makes the action the *entire* content of quantum theory. Planck's constant $\hbar$ — a quantum of pure action — sits at the root of quantum mechanics, while mass, charge, and even spacetime dimension have never been given comparably primitive roles. Meanwhile, attempts to make "stuff" fundamental (point particles, continuum fields, strings) keep generating infinities and ontological puzzles, while action keeps quietly working.

We take the hint seriously and invert the ontology:

> **There are no things. There are only actions. An action is a function; physics is the study of how functions compose, defer, and evaluate.**

"Stuff" — mass, energy, fields, particles, spacetime itself — is what certain patterns of action look like from inside.

### 1.2 Why *purely functional* functions

If an action is a function, we must say what kind. The mathematics of computation offers two broad options: functions with side effects (imperative programs, mutable state) and *pure* functions (the $\lambda$-calculus tradition: output depends only on input; evaluation changes nothing but the term itself). We choose purity, and not for aesthetic reasons:

1. **Purity gives confluence.** The Church–Rosser theorem guarantees that pure reduction systems produce results independent of evaluation order. We will show that this single theorem reproduces the observer-independence at the heart of relativity. An imperative universe would need to postulate what a pure universe *proves*.
2. **Purity gives conservation.** A pure function cannot leak or smuggle resources; every cost is visible in its type and its grade. This turns Noether's theorem into a tautology about referential transparency (Section 6).
3. **Purity gives quantum structure for free.** Call-by-need evaluation (laziness) naturally produces unevaluated shared subcomputations — *thunks* — whose behavior under forcing reproduces superposition, entanglement, and measurement-like collapse without any extra postulates (Section 8).
4. **Purity is the strongest possible ontological economy.** No state, no time, no space, no things — only terms and reduction.

### 1.3 Rigor policy

The framework is new and speculative; we therefore adopt a strict labeling discipline throughout:

- **Definition / Theorem / Proof** — statements inside the calculus, provable with elementary mathematics.
- **Postulate** — a proposed identification between a calculus notion and a physical notion. Postulates are few (six) and stated once, in Section 3.
- **Conjecture** — a claim we believe provable or testable but do not establish here.

The calculus itself is intentionally small: four term formers, one type former, three reduction rules, one cost function. Everything else is derived.

---

## 2. The Action Calculus $\Lambda_{\!A}$: Syntax, Types, Reduction, Cost

### 2.1 Syntax

Fix a finite alphabet of **atomic actions** $\Sigma = \{\alpha_1, \dots, \alpha_N\}$. The set of **terms** (actions) is generated by:

$$
t \;::=\; x \;\mid\; \alpha \;\mid\; \lambda x.\, t \;\mid\; t\,t \;\mid\; \mathbf{let}\; x = t \;\mathbf{in}\; t
\tag{2.1}
$$

where $x$ ranges over a countable set of variables and $\alpha \in \Sigma$.

**Reading.** $\lambda x.\,t$ is *action abstraction*: an action awaiting an input action. $t\,u$ is *application*: action $t$ applied to action $u$. $\mathbf{let}\;x = u\;\mathbf{in}\;t$ is *deferral with sharing*: $u$ is bound as a named thunk, not evaluated until (and unless) demanded inside $t$, and if demanded twice it is computed once and shared. Composition is definable:

$$
f \circ g \;:=\; \lambda x.\, f (g\, x).
\tag{2.2}
$$

**Remark (purity).** There is no assignment, no sequencing-with-state, no I/O, no environment mutation. Substitution replaces text with text; nothing is ever overwritten. This is the whole point: the ontology contains *only* functions and their composition.

### 2.2 Types

There is a single base type $\mathsf{E}$ — read *event* — and one type former:

$$
\tau \;::=\; \mathsf{E} \;\mid\; \tau \to \tau .
\tag{2.3}
$$

Typing rules are the standard simply-typed rules:

$$
\frac{x:\tau \in \Gamma}{\Gamma \vdash x : \tau}\;(\text{var})
\qquad
\frac{\vdash \alpha : \mathsf{E}\!\to\!\mathsf{E}}{\phantom{\Gamma \vdash \alpha : \mathsf{E}\!\to\!\mathsf{E}}}\;(\text{atom})
$$

$$
\frac{\Gamma, x:\sigma \vdash t : \tau}{\Gamma \vdash \lambda x.\,t : \sigma \to \tau}\;(\to\!\mathrm{I})
\qquad
\frac{\Gamma \vdash t : \sigma \to \tau \quad \Gamma \vdash u : \sigma}{\Gamma \vdash t\,u : \tau}\;(\to\!\mathrm{E})
\qquad
\frac{\Gamma \vdash u : \sigma \quad \Gamma, x:\sigma \vdash t : \tau}{\Gamma \vdash \mathbf{let}\,x{=}u\,\mathbf{in}\,t : \tau}\;(\text{let})
\tag{2.4}
$$

Every atomic action has type $\mathsf{E}\to\mathsf{E}$: atoms transform events into events. **Events are not primitive objects; an event is a value of base type — i.e., a fully evaluated residue of actions.** Values of type $\mathsf{E}$ are built from a distinguished nullary event $\bullet : \mathsf{E}$ by application of atoms; we write $\alpha_1 \alpha_2 \cdots \alpha_k\,\bullet$ as $\langle \alpha_1,\dots,\alpha_k\rangle$, a *history chain*.

**Definition 2.1 (Closed physical term).** A term $t$ is *physical* if it is closed (no free variables) and well-typed. The universe $\mathcal{U}$ (Postulate P1) is a physical term.

**Theorem 2.2 (Safety; standard).** Well-typed closed terms never get stuck: reduction preserves typing (type preservation) and a closed well-typed term is either a value or reducible (progress).

*Proof.* Standard induction on typing derivations; see Appendix A. $\blacksquare$

*Physical gloss (informal until Section 3): the universe cannot crash. There is no "type error" in reality.*

### 2.3 Reduction

Reduction has exactly three rules, applied to any redex anywhere in a term (we write $t[u/x]$ for capture-avoiding substitution):

$$
(\lambda x.\,t)\,u \;\longrightarrow_\beta\; t[u/x]
\tag{$\beta$}
$$

$$
\alpha\, \langle h \rangle \;\longrightarrow_\delta\; \langle \alpha \mathbin{::} h \rangle
\tag{$\delta$}
$$

$$
\mathbf{let}\; x = u \;\mathbf{in}\; t \;\longrightarrow_{\mathbf{let}}\; t[u/x]
\tag{$\mathbf{let}$}
$$

Rule ($\delta$) is the only rule that *does* anything at base type: an atom applied to a history extends the history. Rules ($\beta$) and ($\mathbf{let}$) are administrative — they rearrange work without producing events.

**Operational discipline (laziness).** Evaluation is **call-by-need**: in an application $t\,u$, the argument $u$ is *not* reduced before substitution; it is substituted as a suspended computation (thunk), and reduced only if the value of $t\,u$ demands it; a demanded thunk is evaluated once and the result shared by all occurrences (graph reduction). The $\mathbf{let}$-form makes this discipline explicit: $\mathbf{let}\;x = u\;\mathbf{in}\;t$ defers $u$ until $x$ is demanded.

**Definition 2.3 (History / reduction path).** A *history* of $t$ is a reduction sequence $t = t_0 \to t_1 \to \cdots \to t_n$. A history is *maximal* if $t_n$ is in normal form (no redex).

**Definition 2.4 (Value / normal form).** A value is a term in normal form. At type $\mathsf{E}$ values are exactly the history chains $\langle \alpha_{i_1},\dots,\alpha_{i_k}\rangle$.

### 2.4 The cost grading

**Definition 2.5 (Cost).** Every single reduction step ($\beta$, $\delta$, or $\mathbf{let}$) has cost $1$. The **cost of a history** $\mathfrak{h} = (t_0 \to \cdots \to t_n)$ is $\mathrm{cost}(\mathfrak{h}) = n$. For a term $t$ with a normal form, the **grade** $\gamma(t)$ is the cost of the *shortest* maximal history of $t$:

$$
\gamma(t) \;:=\; \min\{\, n \;:\; t \to^n \mathrm{nf}(t) \,\}.
\tag{2.5}
$$

**Postulate (foreshadowed, P5 in Section 3).** The physical action of a history $\mathfrak{h}$ is $S[\mathfrak{h}] = \hbar\cdot\mathrm{cost}(\mathfrak{h})$.

Note what this buys immediately: because costs are integers, **action is quantized by construction**. We do not postulate $\hbar$; $\hbar$ is the unit of counting steps. This is made precise as Theorem 6.4.

### 2.5 Three classical theorems the universe inherits

Because $\Lambda_{\!A}$ is a pure, simply-typed reduction system with sharing, it inherits three classical results, each of which becomes a pillar of the physics:

**Theorem 2.6 (Confluence / Church–Rosser).** If $t \to^* u$ and $t \to^* v$, then there exists $w$ with $u \to^* w$ and $v \to^* w$. Hence normal forms, when they exist, are unique.

*Proof.* The $\beta/\mathbf{let}$ fragment is the pure $\lambda$-calculus with let, which is confluent by the standard Tait–Martin-Löf argument; the $\delta$ rules are left-linear and non-overlapping (they fire only on atoms applied to distinct history chains, and different atoms do not interfere since $\delta$ has no critical pairs), so the combined system is confluent by the orthogonal-combination lemma. Details in Appendix A. $\blacksquare$

**Theorem 2.7 (Strong normalization).** Every well-typed term reduces to a normal form in finitely many steps, under every reduction strategy.

*Proof.* Simply-typed $\lambda$-calculus is strongly normalizing (Tait's reducibility method); $\mathbf{let}$ and non-overlapping $\delta$ preserve the argument. Appendix A. $\blacksquare$

**Theorem 2.8 (Cost invariance under evaluation order for $\delta$).** Any two maximal histories of the same term contain the same number of $\delta$-steps.

*Proof.* Each $\delta$-step appends exactly one atom to one history chain; atoms are consumed (applied) exactly once because typing is affine in the $\delta$-relevant fragment: an atom $\alpha : \mathsf{E}\to\mathsf{E}$ can fire only when applied to an event value, the application site is unique in the term tree, and $\beta/\mathbf{let}$ steps only permute or copy *unevaluated* thunks — but call-by-need sharing evaluates each demanded thunk once (Definition 2.3 discipline), so copying never duplicates a *forced* $\delta$. Hence the multiset of fired atoms is an invariant of the term, not of the strategy. $\blacksquare$

**Remark.** Theorem 2.8 is the seed of energy conservation (Section 6): the "event-producing work" of an action does not depend on *when* or *in what order* it is performed. Administrative ($\beta/\mathbf{let}$) steps can vary with strategy; event steps cannot. This asymmetry — conserved event-work, non-conserved administrative work — will map to the distinction between energy and entropy.

---

## 3. The Physical Postulates

The calculus is pure mathematics. To get physics we need a dictionary. We compress the entire ontology into six postulates — no more.

> **P1 (Universe).** The physical universe is a single closed, well-typed term $\mathcal{U}$ of $\Lambda_{\!A}$. All physical content of reality is reduction-theoretic content of $\mathcal{U}$.

> **P2 (Purity / referential transparency).** Every physical action is a pure function: its output depends only on its input, and evaluation has no side effects. There is no physical operation outside the three reduction rules.

> **P3 (Compositionality).** The physical meaning of a composite action is exhausted by the meanings of its parts and their mode of composition. (Reality is a homomorphic image of term structure.)

> **P4 (Laziness / potentiality).** Evaluation is call-by-need. A subcomputation that is never demanded has no definite value and produces no events. Demanding a value ("observation") forces its thunk once, irrevocably, and shares the result with every referencer.

> **P5 (Cost = action).** The physical action of any history is $S = \hbar \cdot \mathrm{cost}$, with $\hbar$ a universal constant converting step-count into units of action. Interference between alternative histories of the same endpoints is weighted by $e^{iS/\hbar} = e^{i\,\mathrm{cost}}$ — i.e., the phase of a path is its step count, an integer (the constant $1$ radian per step is a choice of phase units, fixed once and for all).

> **P6 (Finiteness / computability).** Physically realizable subterms of $\mathcal{U}$ are finite, and every physically realizable family of histories is recursively enumerable.

Everything in Sections 4–10 is either a theorem of $\Lambda_{\!A}$ or a consequence of these six postulates. No further ontology is permitted: no points, no instants, no substances, no background.

**Remark 3.1 (On P5's phase).** Assigning phase $e^{i\,\mathrm{cost}}$ makes the *least-cost* history the *stationary-phase* history: varying the strategy at fixed endpoints changes administrative ($\beta/\mathbf{let}$) step counts, and the sum $\sum_{\text{paths}} e^{i n}$ is dominated by the paths whose cost is stationary under small variations — the shortest ones (Section 6.4). Thus the principle of least action is not an axiom here but the saddle-point of a path sum whose weights are fixed by P5.

**Remark 3.2 (The dictionary at a glance).**

| $\Lambda_{\!A}$ notion | Physical notion |
|---|---|
| Term (action) | Physical process / "what happens" |
| Event value $\langle h\rangle$ | Localized physical event, with history $h$ |
| Reduction step | Elementary becoming; one tick of local time |
| Data dependence between steps | Causal order |
| Reduction strategy (order) | Observer / foliation |
| $\delta$-step count | Conserved event-work $\propto$ energy |
| Shortest-history grade $\gamma$ | Stationary action |
| Cost of redirecting an action | Mass (inertia) |
| Shared environment of deferred bindings | Field |
| $\alpha$-equivalence (bound renaming) | Gauge symmetry |
| Recursion fixed point | Particle (persistent localized process) |
| Unevaluated thunk | Superposition |
| Shared thunk | Entanglement |
| Forcing a thunk | Measurement |
| Term size bound in a region | Information/entropy bound |
| Non-normalizing subterm | Irreversible becoming / open future |

Sections 4–9 unpack each row into definitions and theorems.

---

## 4. Emergence I — Time, Causality, and the Light Cone

### 4.1 Time is reduction order

**Definition 4.1 (Event-step).** An *event-step* of a history $\mathfrak h$ is the occurrence of a $\delta$-rule firing: a pair $(s, \alpha)$ where $s$ is the position in the term tree at which $\alpha$ was applied. We write $s_1, s_2, \dots$ for event-steps.

**Definition 4.2 (Causal order).** For event-steps $s_1, s_2$ in a history, write $s_1 \prec s_2$ ("$s_1$ causally precedes $s_2$") if the value consumed at $s_2$ was (partly) produced at $s_1$ — i.e., the history chain to which the atom at $s_2$ applied contains the atom added at $s_1$. The relation $\prec$ extends to a partial order on all event-steps (its transitive closure; acyclicity is immediate since a chain is a finite list and $::$ only appends).

**Postulate-linked definition (time).** *Physical time is the causal order $\prec$.* There is no global time coordinate; there is only "which event-steps fed which." A **clock** is any subterm that emits a periodic chain of event-steps; durations are counted in event-steps along chains.

**Theorem 4.3 (Time is a partial order, not a line).** The set of event-steps under $\prec$ is in general a proper partial order: there exist incomparable pairs $s_1 \nprec s_2 \nprec s_1$.

*Proof.* Take $t = \mathbf{let}\,x = \alpha\,\bullet\,\mathbf{in}\,\mathbf{let}\,y = \beta\,\bullet\,\mathbf{in}\,(x, y)$-type constructions — concretely $t = (\lambda a.\,\lambda b.\, a)\,(\alpha\bullet)\,(\beta\bullet)$ reduced lazily to demand both arguments. The $\delta$-step for $\alpha$ and the $\delta$-step for $\beta$ act on disjoint chains; neither's output is the other's input. Hence incomparable. $\blacksquare$

*Physical gloss: simultaneity — "two events with no causal order" — is not a puzzle in PFD; it is the generic case. What is surprising is not that distant events are unordered but that any two events are ordered at all.*

### 4.2 The light cone is the dependence cone

**Definition 4.4 (Influence bound).** Let $d(s)$ be the depth of an event-step (the length of the dependency chain from the root of the term to $s$). The **future cone** of $s$ is $C^+(s) = \{ s' : s \prec s' \}$; its depth-$n$ slice is $C^+_n(s) = \{ s' \in C^+(s) : d(s') - d(s) = n\}$.

**Theorem 4.5 (Finite propagation speed).** There is a constant $c_0$ such that for every event-step $s$ and every $n$: event-steps in $C^+_n(s)$ whose *term-tree distance* from the site of $s$ exceeds $c_0 \cdot n$ do not exist. In words: influence propagates at a bounded number of edges per dependency level.

*Proof.* A single $\delta$-step appends one atom to one chain; the resulting value can serve as argument only to redexes that were already waiting for a value at that site or at sites reachable by substitution of one thunk — and each $\beta/\mathbf{let}$ step moves a value across a bounded number of term-tree edges (the size of the abstraction body, bounded for finite terms by P6). Hence in $n$ dependency levels, influence crosses at most $n \cdot \max|\text{bodies}|$ edges. Set $c_0$ to that maximum. Finiteness of $\mathcal{U}$'s realizable subterms (P6) bounds the maximum. $\blacksquare$

**Postulate-linked definition (space and $c$).** *Spatial distance* between two event-steps is their term-tree distance in the shared dependency graph (more invariantly: half the length of the shortest dependency path joining them in the undirected sense). Theorem 4.5 then says: there is a universal bound $c$ — the ratio of spatial to temporal extent of any causal influence. **The speed of light is the finite bandwidth of functional dependence.** Nothing about the value of $c$ is postulated; its *existence and universality* are theorems of the calculus plus P6.

### 4.3 Locality and no-signalling

**Theorem 4.6 (No-signalling from locality of substitution).** Let $A$ and $B$ be spatially separated subterms (disjoint in the dependency graph except for a common past). Then forcing (evaluating) a thunk inside $A$ cannot change the set of possible normal forms of any subterm inside $B$, except through shared thunks present in their common past.

*Proof.* Reduction is local rewriting: a redex fires where it is. The only nonlocal structure in the calculus is sharing (P4): two sites holding references to one thunk. If $A$ and $B$ share no thunk, no rewrite inside $A$ touches $B$'s term. If they do share a thunk, the correlation was installed when the shared thunk was *created* — in their common past — not when it was forced. $\blacksquare$

This theorem does double duty: it is the relativistic no-signalling principle, and it is the exact template for the entanglement discussion of Section 8.4 — correlations without communication, because sharing is established at binding time, not at forcing time.

---

## 5. Emergence II — Confluence as Relativity

### 5.1 Observers are reduction strategies

In a pure calculus, *when* and *in what order* redexes fire is a matter of strategy, not of meaning. Call-by-need fixes a discipline but not a total order: between two incomparable redexes (Theorem 4.3), either may fire first.

**Definition 5.1 (Observer / foliation).** An **observer** is a fair sequential reduction strategy: a linear extension of the causal order $\prec$ of $\mathcal{U}$'s histories (every event-step eventually scheduled, no causally-later step scheduled before its predecessors). Two observers are *equivalent* if they linearize the same partial order — physically, if they assign the same causal structure.

*Physical gloss: an observer is a way of "reading out" the universe's computation in a sequence. Different observers slice the same partial order differently — this is the relativity of simultaneity, here a triviality about linear extensions.*

### 5.2 The relativity theorem

**Theorem 5.2 (Observer-independence of outcomes).** Let $\sigma_1, \sigma_2$ be any two observers applied to the same term $t$. Then the normal forms they compute are identical: $\mathrm{nf}_{\sigma_1}(t) = \mathrm{nf}_{\sigma_2}(t)$.

*Proof.* Immediate from confluence (Theorem 2.6) plus strong normalization (Theorem 2.7): every fair strategy terminates, and all terminating strategies reach the unique normal form. $\blacksquare$

**Corollary 5.3 (Invariance of physical law).** Any quantity definable from normal forms and $\delta$-counts alone — event content, energy (Section 6), particle spectra (Section 7.3) — is the same for all observers.

*Physical gloss: the laws of physics are the same for all observers not because of a symmetry postulated of spacetime, but because outcomes in a pure functional universe cannot depend on evaluation order. Relativity is what confluence looks like from inside.*

### 5.3 Lorentz structure from confluence + finite bandwidth

Theorem 5.2 gives order-independence; Theorem 4.5 gives a universal propagation bound $c$. Together they force the familiar kinematics, by an argument standard in the causal-invariance literature: if all foliations of a partially ordered set with a uniform finite propagation bound must yield identical observables, then the coordinate transformations relating foliations are precisely those preserving the cone structure — the Lorentz group (up to the Euclidean alternative, excluded by the indefiniteness of $\prec$: cones are directed).

We state this as a theorem *schema*, since the full reconstruction requires a regularity assumption:

**Definition 5.4 (Homogeneity).** A subterm region is *homogeneous* if its dependency graph is vertex-transitive at coarse grain (all sites look alike after rescaling).

**Theorem 5.5 (Lorentz, conditional).** In homogeneous regions, the group of observer-coordinate transformations that (i) preserve $\prec$, (ii) preserve the bound $c$ of Theorem 4.5, and (iii) map observers to observers, is the Lorentz group $SO(1,3)$ in the large-scale limit where the dependency graph approximates a continuum.

*Proof sketch.* (i) forces transformations to be cone-preserving; (ii) forces them to preserve a single finite speed; (iii) forces them to form a group acting linearly on coarse-grained coordinates. The classification of such groups (Alexandrov–Zeeman type theorem: cone-preserving bijections of the coarse-grained order are orthochronous Lorentz transformations composed with scalings; homogeneity fixes the scaling) completes the argument. The continuum-limit step is the only non-elementary ingredient; see Section 13, Open Problem 1. $\blacksquare$

**Remark 5.6.** Special relativity in PFD is not a postulate about spacetime — there is no spacetime yet — but a theorem about *strategies on a confluent rewrite system with finite bandwidth*. Time dilation has a concrete meaning: an observer whose readout chain traverses a densely shared region (many forced thunks per unit readout) assigns fewer local event-steps to the same global dependency interval — its clock literally ticks less, because less *happened* per readout. This prefigures the gravitational redshift of Section 9.

---

## 6. Emergence III — Energy, Mass, and Conservation Laws

### 6.1 Energy is the $\delta$-count

Recall the reduction rules split into *event-producing* steps ($\delta$: an atom extends a history chain) and *administrative* steps ($\beta$, $\mathbf{let}$: rearranging work). Theorem 2.8 showed the $\delta$-count of a complete evaluation is strategy-independent. This invariance earns the $\delta$-count a physical name.

**Definition 6.1 (Energy).** The **energy** of a term $t$ relative to an observer $\sigma$ is $E_\sigma(t) := \hbar\, \nu_\delta(t)\, f_\sigma$, where $\nu_\delta(t)$ is the number of $\delta$-steps in the complete evaluation of $t$ and $f_\sigma$ is the observer's readout frequency (event-steps scheduled per unit of the observer's own clock chain). Equivalently and more intrinsically: energy is *density of event-work per unit of experienced time*.

**Remark 6.2 (Planck relation).** If $t$ is periodic — a recursion (Section 7.3) whose fixed-point body fires $\nu_\delta$ atoms per cycle — then $E = \hbar \nu_\delta f$ is the Planck relation $E = h f$ with $h = \hbar\nu_\delta$ for a single-atom-per-cycle process ($\nu_\delta = 1$). The Planck relation is thus a *definition of energy as action-rate*, and $\hbar$ is the price of one event.

**Theorem 6.3 (Conservation of energy — the purity Noether theorem).** Energy is conserved in all interactions: if $t \to^* t'$ and evaluation is complete, $\nu_\delta(t) = \nu_\delta(t')$; and under composition, $\nu_\delta(t_1 \circ t_2) = \nu_\delta(t_1) + \nu_\delta(t_2)$.

*Proof.* The first claim is Theorem 2.8. The second: composing $t_1$ after $t_2$ on a chain applies both terms' atoms to the chain; each atom fires once (affinity of $\mathsf{E}\to\mathsf{E}$ usage), so the $\delta$-counts add. No $\delta$ can be created from nothing (the rules have no $\delta$-producing right-hand side other than $\delta$ itself) nor annihilated (substitution cannot delete a demanded application; purity forbids discarding a value that is depended upon) — this is precisely referential transparency. $\blacksquare$

*Physical gloss: energy conservation holds because a pure function cannot smuggle work in or out — every event it will ever produce is fixed by its syntactic content. In standard physics, Noether's theorem trades time-translation symmetry for energy conservation; here time-translation invariance is the strategy-independence of the $\delta$-count, which is what purity means. The correspondence is exact.*

**Theorem 6.4 (Quantization of action).** For every physically realizable history $\mathfrak h$, $S[\mathfrak h] = n\hbar$ for some $n \in \mathbb N$.

*Proof.* Definition of cost (2.5: integer steps) plus P5. $\blacksquare$

The discreteness of action — the foundational empirical fact of quantum theory — is here a theorem about the syntax of finite terms.

### 6.2 Mass is the cost of redirection

What, in a world of pure actions, is inertia? An action's "direction" is its *leading effect*: the head atom it is committed to fire next on its input chain. To redirect an action is to supply additional actions that change that commitment.

**Definition 6.5 (Redirection and mass).** Let $t : \mathsf{E}\to\mathsf{E}$ be a closed action in normal form except for its pending $\delta$ (i.e., $t$ ready to extend a chain). A **redirection** of $t$ is a term $r$ such that $r \circ t$ has a different head atom from $t$ on the same input. The **mass** of $t$ is the minimal grade of a redirection:

$$
m(t) \;:=\; \frac{\hbar}{c^2}\, \min\{\, \gamma(r) \;:\; r \text{ redirects } t \,\}.
\tag{6.1}
$$

**Theorem 6.6 (Mass is positive and additive).** (i) $m(t) \ge 0$, with $m(t) = 0$ iff $t$ can be redirected by administrative steps alone (no new atoms). (ii) For independent parallel actions, $m(t_1 \parallel t_2) = m(t_1) + m(t_2)$.

*Proof.* (i) Grades are non-negative integers; zero grade means $r$ is a pure $\beta/\mathbf{let}$ rearrangement — such actions ("radiation": freely steerable processes) are massless. (ii) A redirection of the pair must redirect both heads; minimal grades on disjoint subterms add, since the disjoint union of minimal histories is minimal (no sharing by independence). $\blacksquare$

**Interpretation.** Mass measures *how much action it costs to change what an action does*. Deeply self-referential actions — recursions that re-instantiate themselves (next section) — are expensive to redirect because a redirector must unwind the recursion: mass scales with recursion depth. This gives a first-principles reason for a *mass spectrum*: particles are recursion fixed points (7.3), and the discreteness of recursion structures implies a discrete spectrum of redirection costs. The mass spectrum of matter is the taxonomy of stable loops in the universe's source code.

### 6.3 Momentum and the on-shell relation

**Definition 6.7 (Momentum).** The momentum of an action is the spatial density of its event-work: $p := \hbar\,\nu_\delta / \ell$, where $\ell$ is the spatial extent (term-tree distance, Definition under Theorem 4.5) over which its $\delta$-steps are distributed per readout interval.

**Theorem 6.8 (On-shell relation, conditional on 5.5).** In homogeneous regions, Definitions 6.1, 6.5, 6.7 satisfy $E^2 = p^2 c^2 + m^2 c^4$.

*Proof sketch.* Under Theorem 5.5, coarse-grained observers are related by Lorentz transformations; $E$ and $p$ are the temporal and spatial densities of the same invariant $\delta$-count $\nu_\delta$, hence transform as components of a 4-vector whose invariant norm is fixed by the redirection cost (6.1), i.e. $mc^2$. Lorentz invariance of the norm gives the relation. $\blacksquare$

### 6.4 Least action as stationary phase

**Theorem 6.9 (Classical limit).** Let $H(q_i, q_f)$ be the set of histories of a term with fixed initial and final values, weighted by $e^{i\,\mathrm{cost}(\mathfrak h)}$ (P5). If costs are large compared with $1$ and vary smoothly over $H$, the sum $\sum_{\mathfrak h} e^{i\,\mathrm{cost}(\mathfrak h)}$ is dominated by histories of stationary — generically minimal — cost; i.e., the classical trajectory realizes the least-action path.

*Proof.* Standard stationary-phase: contributions from histories whose cost differs from the stationary value $\gamma$ by $\Delta$ acquire relative phase $\Delta$ (integer radians per step); for $\Delta \gg 1$ these cancel in the sum, leaving a $O(1)$-neighborhood of $\gamma$. Minimality is generic since $\gamma$ is a minimum of a bounded-below integer function. $\blacksquare$

The Euler–Lagrange equations are then recovered in the continuum limit by the usual argument applied to the cost function: $\delta \gamma = 0$ along the dominant history. **The principle of least action is the statement that the universe's evaluator, sampled coarsely, appears to take the cheapest reduction path — because all the expensive ones interfere to zero.**

---

## 7. Emergence IV — Fields, Gauge Symmetry, and Particles

### 7.1 Fields are shared environments

Consider a family of actions $t_1, \dots, t_k$ at different sites, all containing free references to the same deferred bindings:

$$
t_i = \lambda \phi.\;(\text{local action using } \phi), \qquad \text{all evaluated in the environment } \rho = \{ \phi \mapsto u \}.
$$

**Definition 7.1 (Field).** A **field** is a shared environment: a finite map $\rho$ from names to thunks, referenced by many actions. The **value of the field at a site** is the normal form of the referenced thunk *as demanded at that site*. A **field excitation** is a $\delta$-step fired while forcing a shared thunk.

**Theorem 7.2 (Fields mediate without stuff).** If actions $A$ and $B$ interact only through a shared environment $\rho$, then (i) the interaction is local in the dependency graph (each forces thunks where it is), (ii) the mediation propagates at most at the bound $c$ (Theorem 4.5, applied to thunk forcing chains), and (iii) no ontology beyond terms, bindings, and reduction is required.

*Proof.* (i) and (ii) are immediate from the locality of reduction and Theorem 4.5 (forcing a thunk is a reduction). (iii) is a tautology given P1–P3. $\blacksquare$

*Physical gloss: a field is not a fluid filling space; it is a shared lookup table of deferred actions. "Space filled with field" = "many sites holding references to the same environment." The vacuum is an environment in which nothing has yet been forced.*

### 7.2 Gauge symmetry is α-equivalence

In the $\lambda$-calculus, bound-variable names are meaningless: $\lambda x.\,t \equiv_\alpha \lambda y.\,t[y/x]$. This **$\alpha$-equivalence** is the most trivial fact about the calculus — and, mapped through P3, one of the deepest facts about physics.

**Theorem 7.3 (Gauge invariance).** Let $t$ be any physical term and $\pi$ any permutation of bound names that is the identity on observationally demanded values. Then $\pi(t) \equiv t$ in every physical respect: same normal forms, same costs, same $\delta$-counts.

*Proof.* $\alpha$-equivalent terms have identical reduction behavior by definition of capture-avoiding substitution; cost is a function of reduction steps. $\blacksquare$

**Interpretation.** The freedom to rename local labels without physical effect *is* gauge freedom. A gauge transformation is a site-dependent renaming $\pi$; the requirement that physics be invariant is automatic in a language where names don't matter. Moreover:

**Theorem 7.4 (Gauge bosons are massless).** The action that *implements* a renaming — the "connection" term carrying name-information between sites — is pure administration: it fires no $\delta$-steps of its own, hence has zero redirection cost, hence zero mass.

*Proof.* A renaming changes only names, not event content: its evaluation contains only $\beta/\mathbf{let}$ steps, so by Definition 6.5 it can be "redirected" (altered) at zero grade, $m = 0$. $\blacksquare$

*Physical gloss: the photon and gluons are massless because gauge bosons are the plumbing of the namespace, and plumbing produces no events. (The weak bosons' masses then require, and in this framework are defined by, thunk-forcing friction — a Higgs-like environment in which renaming is not free; see Open Problem 4.)*

### 7.3 Particles are recursion fixed points

Nothing in the calculus so far *persists*. Values are produced and consumed. Persistence requires an action that, when run, produces (a copy of) itself:

**Definition 7.5 (Particle).** A **particle** is a minimal recursion fixed point: a closed term $p$ of smallest size such that, in the ambient environment, $p \to^* C[p]$ for some non-trivial context $C$, with the self-reference traversed at least once per evaluation cycle — i.e., $p$ re-instantiates itself while firing at least one $\delta$ per cycle. The **species** of $p$ is its equivalence class under renamings and administrative rearrangement.

The standard fixed-point combinator $\mathsf{Y} = \lambda f.\,(\lambda x.\,f(x\,x))(\lambda x.\,f(x\,x))$ supplies existence: $\mathsf{Y} g \to^* g (\mathsf{Y} g)$. (Note: $\mathsf{Y} g$ is not strongly normalizing for all $g$; Theorem 2.7 applies to the terminating fragment. Particles are precisely the controlled, typed recursions that produce one $\delta$ per unfold and remain productive — the *guarded* recursions.)

**Definition 7.6 (Guarded particle).** A particle $p = \mathsf{Y} g$ is **guarded** if every recursive self-reference in $g$ occurs underneath at least one atom application (one $\delta$). Guardedness makes each unfold produce an event before recurring — the particle "ticks."

**Theorem 7.7 (Stability and decay).** (i) A guarded particle in a static environment persists: its evaluation is productive (emits an infinite chain of events, one per cycle). (ii) A particle destabilizes — decays — exactly when the environment supplies an action that matches an alternative unfold of lower grade; decay products are the sub-actions of the cheaper unfold, and total $\delta$-count (energy) is conserved across the decay.

*Proof.* (i) Guardedness: each unfold fires $\ge 1$ atom before the recursive call, so the chain grows by at least one event per cycle — productivity. (ii) A cheaper alternative unfold, if present in the environment, dominates the path sum (Theorem 6.9's stationary-phase logic applied to the two branches); conservation is Theorem 6.3. $\blacksquare$

**Interpretation.** An electron is a tight, cheap, guarded loop — minimal recursion depth, hence small mass (6.2) and no cheaper unfold (stability). A muon is the same *shape* of loop at greater recursion depth — same charge-relevant structure, higher redirection cost, and a cheaper unfold exists (decay). The particle spectrum is the taxonomy of small guarded fixed points of the universal term. The discreteness of the spectrum is a theorem: there are countably many terms of each finite size.

### 7.4 Spin, statistics, and identity

**Theorem 7.8 (Indistinguishability).** Two occurrences of the same closed particle term are not merely similar but *identical*: there is no property definable in the calculus that distinguishes them, because purity (P2) forbids any hidden label.

*Proof.* Any distinguishing probe would be a context giving different results for the two occurrences; but they are syntactically identical closed terms, and reduction is a function of syntax. $\blacksquare$

Quantum indistinguishability — the basis of quantum statistics — is thus immediate: *two electrons are the same function occurring twice.* The exchange phase (boson vs. fermion) corresponds to the two confluent orders of composing shared thunks being equal up to a sign, i.e., to the two homotopy classes of exchange paths in the dependency graph; we record the full derivation of the spin-statistics connection as Conjecture C2 (Section 13), since it requires the continuum topology of the coarse-grained graph.

---

## 8. Quantum Phenomena from Laziness

Everything in this section follows from one decision already made: **P4 — call-by-need evaluation with sharing.** No new physics is added.

### 8.1 Superposition is the unevaluated thunk

**Definition 8.1 (Superposition).** A **superposition** is a demanded-but-not-yet-forced thunk whose complete evaluation passes through a *choice point*: a subterm $(\lambda x.\,b)\,u$ where the environment offers several distinct reduction continuations $u_1, u_2, \dots$ with weights $w_k = e^{i\,\mathrm{cost}_k}$ (P5), differing in their $\delta$-content. Before forcing, the thunk has no value — only the *set* of its possible histories.

*Physical gloss: an unevaluated thunk is not "a definite value we are ignorant of." It is a syntactic object whose value does not yet exist. Purity forbids hidden variables (Theorem 8.4 below), so the indefiniteness is ontic, not epistemic. Superposition is the normal state of affairs in a lazy universe; definiteness is the exception, purchased by forcing.*

### 8.2 Interference is path-sum over reductions

**Definition 8.2 (Amplitude).** The amplitude for a thunk $u$ to force to value $v$ is the sum over histories:

$$
A(u \Rightarrow v) \;=\; \sum_{\mathfrak h :\, u \to^* v} e^{i\,\mathrm{cost}(\mathfrak h)} .
\tag{8.1}
$$

**Theorem 8.3 (Composition law).** Amplitudes compose multiplicatively over sequential evaluation and additively over alternative histories: if $u \Rightarrow w$ must pass through intermediate forced value $v'$, then $A(u\Rightarrow w) = \sum_{v'} A(u\Rightarrow v')\,A(v'\Rightarrow w)$.

*Proof.* Histories concatenate; costs add; exponentials of sums multiply. Summing over the intermediate value partitions the path set. $\blacksquare$

This is the Feynman composition law — the seed of the Schrödinger equation, which appears in the continuum limit of (8.1) by the standard path-integral argument, with the cost function playing the role of the classical action (Theorem 6.9).

### 8.3 No hidden variables — a theorem

**Theorem 8.4 (Purity excludes local hidden states).** There is no assignment of additional internal state to a thunk such that (i) the forcing outcome is a function of the state, and (ii) the state is unaffected by distant forcings, unless the state is itself part of the term — i.e., was established in the common past.

*Proof.* By P2, a term's evaluation behavior is a function of its syntax and its (shared) environment. Any "state" satisfying (i) would have to be encoded in the syntax or the environment. Encoding in the environment is exactly sharing — which by Theorem 4.6 can only have been established in the common past. $\blacksquare$

*Physical gloss: this is the PFD reading of Bell-type no-go results. The framework does not escape them — it explains them: the "hidden variable" is the shared thunk, and it is nonlocal in exactly the benign sense of Theorem 4.6 — correlations are installed at binding time, revealed at forcing time, and never transmitted.*

### 8.4 Entanglement is sharing

**Definition 8.5 (Entanglement).** Two sites are **entangled** if they hold references to the same unevaluated thunk: $\mathbf{let}\; x = u\;\mathbf{in}\; (\dots x \dots) \; (\dots x \dots)$ with the two occurrences causally separated after binding.

**Theorem 8.6 (Perfect correlation without signalling).** If sites $A$ and $B$ force the same shared thunk $u$, they obtain the same value, and neither learns anything about whether or when the other forced.

*Proof.* Call-by-need sharing (Definition 2.3 discipline): the first forcing evaluates $u$ once; all references see the single resulting value. No-signalling is Theorem 4.6. $\blacksquare$

**Theorem 8.7 (Monogamy).** A thunk can be shared by exactly the references created at binding time; forcing consumes it. In particular, maximal two-party entanglement cannot be extended to a third party after the fact.

*Proof.* Creating a new reference to $u$ requires a $\mathbf{let}$-binding of $u$, which is a term-construction act occurring in the common past; after separation (disjoint dependency futures), no reduction inside $A$ or $B$ can introduce a new shared reference (locality of rewriting, Theorem 4.6). Forcing replaces the thunk by a value; a value forced again yields itself, carrying no further correlation-generating capacity. $\blacksquare$

*Physical gloss: entanglement is not a mysterious connection; it is the most mundane feature of lazy functional programming — shared references to a lazy computation. The "spooky action at a distance" is just the first `force` memoizing a value that a distant alias then reads. The universe runs call-by-need, and EPR correlations are its memo table.*

### 8.5 Measurement is forcing

**Definition 8.8 (Measurement).** A **measurement** is the forcing of a shared thunk to weak head normal form by a chain of demand originating in an observer (a readout strategy, Definition 5.1). The **outcome** is the value produced; the **record** is the history chain extension (a $\delta$-step — measurement produces an event).

**Theorem 8.9 (Irreversibility and definiteness of records).** Once forced, a thunk stays forced: subsequent references read the memoized value. Records are therefore permanent and single-valued for all observers.

*Proof.* Sharing semantics: a forced thunk is replaced by its value in the environment; confluence (Theorem 2.6) makes the value strategy-independent. $\blacksquare$

**The measurement problem, dissolved.** In PFD there is no special "collapse" dynamics and no measurement axiom. There is one dynamics — reduction — and two regimes: *unevaluated* (thunk: superposition, interference among continuations) and *forced* (value: definite, shared, permanent). "Collapse" is the name we give to the transition a lazy evaluator performs on every memoized reference, everywhere, all the time. What the standard formalism calls "the measurement problem" is the price of describing a call-by-need universe in a call-by-value language.

**Remark 8.10 (Born weights).** The probability weights of outcomes are not yet derived from counting alone; P5 fixes phases, and Theorem 8.3 fixes composition, but the modulus rule $|A|^2$ requires a measure on the set of continuations. We conjecture it follows from typicality of strategies (almost every fair observer samples continuations in proportion to squared amplitude, by a self-locating argument over equivalent readouts) — recorded as Conjecture C1, Section 13.

---

## 9. Gravity as Evaluation-Cost Geometry

### 9.1 The core idea

In Sections 4–5, temporal experience is readout of the causal order, and the uniformity of readout (homogeneity, Definition 5.4) yielded flat Lorentz structure. Now ask: what if the *cost density* is not uniform? A region densely packed with recursion fixed points (particles, Section 7.3) is a region where evaluation is expensive: every readout step forces many deep thunks.

**Definition 9.1 (Cost density and gravitational potential).** The **cost density** $\kappa$ at a site is the number of reduction steps (of all kinds) required per unit of readout advance, coarse-grained over the site. The **gravitational potential** is $\Phi := -c^2 \ln(\kappa / \kappa_0)$ relative to empty-region density $\kappa_0$.

**Theorem 9.2 (Time dilation).** An observer reading out inside a high-$\kappa$ region assigns fewer local event-steps per unit of the global dependency order than an observer in a low-$\kappa$ region: its clock runs slow by the factor $\kappa_0/\kappa$, i.e., $d\tau = dt\,(1 + \Phi/c^2)$ to first order.

*Proof.* The observer's clock counts its own forced $\delta$-steps (Definition of clock, 4.1). Forcing its way through $\kappa$ steps of dense evaluation per readout yields proportionally fewer events per global interval. Expressing the density ratio as a potential via Definition 9.1 and expanding $\ln$ to first order gives the stated factor. $\blacksquare$

*Physical gloss: gravitational time dilation is evaluation drag. A clock near a massive object ticks slowly because the universal evaluator is busy — the mass is a deep recursion whose thunks congest the local reduction fabric.*

### 9.2 Curvature and the field equation (conditional)

**Theorem 9.3 (Geodesic motion, conditional on 5.5 and continuum limit).** In the continuum limit of a slowly varying cost density, the stationary-cost histories (Theorem 6.9) of a test action are geodesics of the metric $ds^2 = -\left(1 + 2\Phi/c^2\right) c^2 dt^2 + d\vec{x}^{\,2}$ to first post-Newtonian order.

*Proof sketch.* Stationary-phase dominance (6.9) makes test actions extremize total cost; cost per unit readout is $\kappa$, so the effective action is $\int \kappa\, d(\text{readout})$; extremizing this in a slowly varying $\kappa$ is Fermat's principle in a medium with refractive index $\kappa$, which by Theorem 9.2's clock factor is the weak-field metric above; geodesics of that metric reproduce Newtonian acceleration $\vec a = -\nabla\Phi$. $\blacksquare$

**Conjecture C3 (Field equation).** In the full theory, cost density $\kappa$ is sourced by the recursion content of the region via a relation whose continuum limit is the Einstein equation $G_{\mu\nu} = (8\pi G/c^4)\,T_{\mu\nu}$, with $G$ emerging from the stiffness of the dependency graph (the cost of re-routing shared references). The precise combinatorial statement is Open Problem 2.

*Physical gloss: matter tells evaluation where to be expensive; expensive evaluation tells matter which paths are cheap. Gravity is the supply-and-demand curve of computation.*

### 9.3 Thunk gravity — unforced computations still weigh

A striking consequence: cost density includes **unevaluated** thunks. A deep, unforced thunk contributes to $\kappa$ because its *structure* must be traversed, copied, and kept consistent by the evaluator even before its value is demanded — deferral is not deletion.

**Prediction (preview of Section 11, P-4).** Regions rich in unforced computation gravitate without radiating events. A universe that defers a great deal of evaluation would contain gravitating influence with no corresponding event-emission — matching the phenomenology ascribed to dark matter. The quantitative ratio of thunk-gravity to event-gravity is fixed by the deferral statistics of the vacuum term; estimating it is Open Problem 3.

### 9.4 Holographic bound

**Theorem 9.4 (Finite information per region).** The number of physically distinct forcings of any subterm contained in a region is bounded by $2^{|\text{term}|}$, and the term size encodable in a region grows at most as its boundary (shared-reference channels crossing the boundary), not its volume.

*Proof.* A finite term of size $n$ has at most $2^{O(n)}$ distinct reduction behaviors (binary syntax). The only way information crosses a region boundary in a pure calculus is through shared references — names in the typing context — whose number is a property of the interface (boundary), not the interior (volume). Hence distinct physical contents scale with boundary channels. $\blacksquare$

*Physical gloss: this is the structural skeleton of the Bekenstein/holographic bound: what a region can be is written on its interface, because the only thing a pure function shows the world is its type.*

---

## 10. The Phenomenology of a Purely Functional Universe

What is it *like* — structurally, not poetically — to inhabit such a universe? This section collects the picture into one coherent description.

### 10.1 There is no stuff

The inventory of reality is: one term, its subterms, their types, their reductions, their costs. Every noun of physics is a verb wearing a costume:

| Noun | The verb underneath |
|---|---|
| Object | An action that re-performs itself (guarded fixed point) |
| Position | A location in the dependency graph |
| Duration | A count of event-steps on a chain |
| Field | A shared table of deferred actions |
| Vacuum | The default environment; the unevaluated |
| Matter | Recursion; computation that refuses to finish |
| Radiation | Administrative action: pure rearrangement, freely steerable, massless |
| Force | A shortcut in composition order made available by a shared environment |
| Law of physics | A theorem of the calculus (confluence, purity, typing) |

### 10.2 Time does not flow; evaluation proceeds

There is no river of time and no moving present. There is the causal order — a static partial order of event-steps — and there are readout strategies threading it. "Now" is the frontier of an observer's forcing: the set of thunks it has demanded so far. The *arrow* of time has a precise origin: reduction is directional. $\beta$-reduction and $\delta$-firing are not invertible as *history production* — the set of histories consistent with a partially evaluated term grows as forcing proceeds.

**Definition 10.1 (Entropy).** The **entropy** of an observer's current state is the logarithm of the number of complete histories of $\mathcal{U}$ consistent with everything the observer has forced so far.

**Theorem 10.2 (Second law).** Entropy is non-decreasing along any observer's readout, and strictly increases at every forcing that has more than one continuation of positive weight.

*Proof.* Each forcing restricts the consistent-history set to those passing through the forced value — a subset (never a superset). Strict increase of *realized* information at a branching forcing; equivalently, the count of *unrealized* alternatives shrinks, so the log of the observer's *remaining ambiguity about the past read as a generic state* grows under coarse description — the standard contraction argument applied to the history lattice. $\blacksquare$

The past is fixed because it is forced; the future is open because it is deferred. **The asymmetry of time is the asymmetry of memoization.**

### 10.3 The universe is its own interpreter

Observers are not outside the system; an observer is a subterm of $\mathcal{U}$ whose evaluation demands values from other subterms — self-application at the grand scale. This has three consequences:

1. **The universe computes itself into being.** There is no external evaluator. P1 says the term exists; P4 says its values exist only where demanded; demand originates within the term. Reality is $\mathcal{U}$ forcing $\mathcal{U}$ — the ultimate self-interpreter.
2. **Observation is participation.** Since every measurement is a $\delta$-step (Theorem 8.8/8.9: measurement produces an event), observing the universe changes the universe's event content — trivially, by adding the record. The observer-observed split is a cut in the dependency graph, not a metaphysical boundary, and the cut can be drawn anywhere (Theorem 5.2 guarantees the answer doesn't depend on where).
3. **The future is genuinely open.** Because $\mathcal{U}$ contains non-normalizing recursions (Section 7.3 showed guarded particles are productive indefinitely), evaluation never completes. There is no final normal form of the whole — only ever-extending weak head normal forms. The universe is not a finished computation being read; it is an ongoing evaluation with no last step. Eternal inflation of the future is a corollary of productivity.

### 10.4 What the night sky is, in this language

A star is a deep guarded recursion, furiously re-instantiating itself, firing $\delta$-steps (photons: administrative rearrangements that carry a renaming of the environment outward — Theorem 7.4's massless plumbing) at the maximal rate its fixed point allows. The space between stars is a sparse environment: few bindings, little demand, long deferrals. Gravity wells are congestion zones where the evaluator's load slows every clock (Theorem 9.2). The cosmic microwave background is the residual memo table of the earliest mass-forcing epoch. Dark structure is the weight of what has been promised but never computed (Section 9.3). And quantum uncertainty is the oldest fact of all: in a lazy universe, almost everything, almost always, is a thunk.

---

## 11. Predictions and Falsifiability

A framework earns the name *physics* only by risking itself. We list the predictions in order of decreasing certainty (the earlier ones are theorems of the calculus read through the postulates; the later ones are conditional or conjectural, and are labeled as such).

**P-1 (Action quantization — already confirmed, but sharpened).** Every physically realizable exchange of action is an integer multiple of $\hbar$ (Theorem 6.4). Beyond standard QM, PFD asserts *all* action is quantized, including gravitational action exchanged across any channel — a claim testable in principle by searches for sub-quantum action transfer, and by the internal consistency of quantum gravity. *Status: theorem.*

**P-2 (Universal rate bound — theorem).** The event-production rate of any localized system is bounded: a term of grade $\gamma$ can fire at most $\gamma$ $\delta$-steps, hence a system of energy $E$ transitions at most $E/h$ times per readout unit — the Margolus–Levitin bound, here a trivial corollary of Definitions 6.1 and 2.5. PFD additionally predicts the bound is *saturable* only by recursion-free terms (loops waste steps on self-reinstantiation), a refinement testable with optimally driven quantum gates. *Status: theorem.*

**P-3 (Gauge boson masslessness — theorem).** All pure-namespace mediation is massless (Theorem 7.4). Any confirmed nonzero photon mass falsifies the identification of gauge symmetry with $\alpha$-equivalence. Conversely, weak-boson masses require environmental renaming friction; PFD predicts their mass ratios are recursion-depth ratios of the friction environment — a computable constraint once the vacuum term is modeled. *Status: theorem + conjectural extension.*

**P-4 (Thunk gravity — dark-sector prediction, conditional on C3).** Unforced computation gravitates (Section 9.3). The specific, falsifiable content: the dark component must (i) gravitate but never radiate events (no electromagnetic thunk-forcing), (ii) cluster where deferral is cheapest — i.e., where ordinary recursion density (baryons) first seeded congestion, explaining halo–galaxy correlation, and (iii) exhibit a universal event-to-thunk cost ratio, hence a *constant* dark-to-baryonic coupling across environments — departures from constant effective $G$ in voids vs. clusters would falsify. *Status: conditional prediction.*

**P-5 (Non-confluence noise — the flagship new-physics prediction).** Confluence (Theorem 2.6) holds exactly for the pure fragment. But the physically realizable universe operates at finite resources (P6), and the orthogonal-combination step of Theorem 2.6 assumes unbounded workspace for completion. When the required completion workspace exceeds what a region can hold (Theorem 9.4's bound), reductions that "should" commute are forced to commit in some order — confluence fails *operationally*. The consequence is tiny, **state-dependent, non-random deviations from exact unitary evolution** that grow with the simultaneous complexity and entanglement of the system — precisely the regime of large-scale quantum computers and macroscopic interferometry. Signature: noise correlated with circuit topology (dependency-graph density), not with temperature or environment alone; absent in low-connectivity circuits of equal size. *Status: conditional prediction; currently the most accessible falsification channel of the whole framework.*

**P-6 (Holographic information bound — theorem).** Distinct physical contents of a region scale with boundary channels, not volume (Theorem 9.4). This reproduces the Bekenstein scaling structurally and predicts the saturation constant is set by the reference-channel capacity of the dependency graph — linking entropy bounds to graph-theoretic conductance, a connection that numerical models of the calculus can fit. *Status: theorem (scaling) + open constant.*

**P-7 (Proper-time discreteness).** Clocks count event-steps (Section 4.1); between two readings of any clock there are finitely many, hence an integer number, of ticks. Proper time is quantized in principle. The tick quantum for a material clock is its recursion period (Section 7.3); PFD predicts *fundamental limits on time-interval metrology* set by clock-composition (recursion depth) rather than by a universal Planck-time floor — composite clocks have composite tick spectra. *Status: theorem (existence of spectrum) + open magnitudes.*

**P-8 (No true randomness — structured pseudorandomness).** All outcomes are determined by the term (Theorem 2.6 + P1); apparent randomness is our ignorance of the reduction path. PFD therefore predicts that "random" quantum outcomes are computable pseudorandom sequences — in principle compressible, in practice incompressible to any sub-universal observer (an observer inside the term cannot enumerate the term, by self-reference limits). The falsifiable edge: in maximal-complexity regimes where P-5 noise operates, outcome statistics should show *computable structure* (finite description length shorter than uniform). *Status: conjecture.*

**Summary table.**

| # | Prediction | Status | Falsification channel |
|---|---|---|---|
| P-1 | Universal action quantization | Theorem | Sub-$\hbar$ action transfer |
| P-2 | Rate bound; saturation only for loop-free dynamics | Theorem | Optimal-control experiments |
| P-3 | Exact masslessness of pure gauge mediators | Theorem | Photon mass measurement |
| P-4 | Thunk gravity as dark sector, constant coupling | Conditional | Void-vs-cluster $G$ tests |
| P-5 | State-dependent non-confluence noise at high complexity | Conditional | Large quantum circuits, interferometry |
| P-6 | Boundary scaling of information content | Theorem (scaling) | Entropy-bound measurements |
| P-7 | Discrete, composition-dependent tick spectra | Theorem (existence) | Ultimate time metrology |
| P-8 | Computable structure in "random" outcomes | Conjecture | Complexity-analysis of outcome streams |

---

## 12. Relation to Existing Science

PFD is deliberately positioned at a crossroads where several mature disciplines meet. We note the precise points of contact — and of departure — without attempting a full review.

**The action tradition.** Maupertuis, Euler, Lagrange, and Hamilton established that classical mechanics is extremal action; Noether (1918) tied conservation to action symmetries; Feynman and Hibbs (1965) made the action the full content of quantum amplitudes. PFD radicalizes this lineage: action is not a functional *of* the ontology, it *is* the ontology, and the extremality principle becomes the stationary phase of a step-count sum (Theorem 6.9).

**The lambda-calculus tradition.** Church's $\lambda$-calculus and the Church–Rosser theorem (1936) supply our core machinery; the simply-typed discipline is Church's and Curry's; call-by-need with sharing is the Wadsworth/Launchbury semantics tradition of lazy functional languages (Haskell's operational heart). Our claim is that this tradition has been unwittingly writing down physics: confluence is relativity (Theorem 5.2), sharing is entanglement (Theorem 8.6), memoization is the arrow of time (Section 10.2), and $\alpha$-equivalence is gauge invariance (Theorem 7.3).

**Categorical and logical physics.** The Curry–Howard correspondence (proofs as programs) and its categorical home (cartesian closed categories) are the natural habitat of P3's compositionality; functorial quantum field theory in the sense of Atiyah and Segal already treats quantum theory as a structure-preserving map between composition systems — PFD can be read as the proposal that the functor is the identity: the composition system *is* the physics. Girard's linear logic, with its resource-sensitive typing, shadows our affine use of atoms and the resulting conservation laws (Theorem 6.3). Milner's *action calculi* (1996) coined our title's phrase in a neighboring sense — a calculus of interactive processes; the present work shares the conviction that interaction, not substance, is fundamental.

**Computational universe programs.** Wheeler's "it from bit," Lloyd's computational-universe bounds (2000), and 't Hooft's cellular-automaton interpretation all argue that physics is computation underneath. Closest in spirit and method is Wolfram's *Physics Project* (2020): spacetime as a rewrite system, causal invariance yielding relativity, multiway graphs yielding quantum mechanics. PFD differs in three ways: (i) the rewrite system is specifically the *pure functional* one, so confluence, purity, and typing — rather than being emergent statistical properties — are exact theorems available from line one; (ii) quantum mechanics arises from *laziness and sharing*, not from multiway branching, which keeps the universe single-valued and makes measurement a forcing event rather than a branch choice; (iii) action, cost, and $\hbar$ are native (Definitions 2.5, P5), rather than appended.

**Bound literature.** The Margolus–Levitin rate bound, the Bekenstein entropy bound, and Lloyd's ultimate laptop limits appear here as theorems of term finiteness and interface typing (P-2, P-6) rather than as independent physical postulates — evidence, we suggest, that these bounds were always facts about computation wearing physical clothes.

---

## 13. Open Problems

**OP-1 (Continuum limit).** Theorem 5.5's Lorentz conclusion requires a rigorous coarse-graining theorem for dependency graphs of large guarded-recursion systems — a "hydrodynamics of $\lambda$-terms." Nothing in the calculus currently guarantees that the large-scale limit is a smooth 3+1 geometry; dimensionality itself should emerge from graph growth exponents. *This is the framework's single most important mathematical gap.*

**OP-2 (The vacuum term and $G$).** Conjecture C3 requires identifying the vacuum environment $\rho_0$ and computing its reference-rerouting stiffness, which would fix $G$ in units of $\hbar, c$ — a derivation of Newton's constant from recursion statistics.

**OP-3 (Deferral statistics of the vacuum).** The dark-sector ratio of P-4 requires counting unforced-thunk weight in $\rho_0$. A toy computation on random guarded-recursion ensembles is feasible now and would either produce a plausible dark fraction or kill the idea.

**OP-4 (Electroweak friction).** Modeling the Higgs mechanism as renaming friction in the namespace (Section 7.2's gloss on weak-boson mass) requires a typed account of *symmetry-breaking environments* — bindings whose forcing cost depends on depth.

**OP-5 (Born rule).** Conjecture C1: derive $|A|^2$ from typicality over fair strategies. The self-locating argument needs a measure on observers, which needs the continuum limit (OP-1).

**OP-6 (Numerical micro-universes).** Appendix B defines a 2-atom toy universe. Systematic simulation of such toy universes — extracting their effective dimension, cone structure, spectra, and noise (P-5) — is immediately doable and would discipline all of the above.

---

## 14. Conclusion

We have built the smallest machine we know that can host a universe: a pure, typed, lazy calculus of actions, graded by a discrete cost. Into it we put six postulates; out of it come — as theorems, not analogies — time, causality, a universal speed limit, observer-independence, energy and its conservation, mass as inertia, gauge invariance and massless mediators, particles as self-reproducing processes, superposition, entanglement, measurement, the arrow of time, the discreteness of action, and the holographic scaling of information. Gravity appears as the economics of evaluation cost, and the open future as the productivity of recursion.

The framework risks itself: it predicts exact masslessness of gauge mediators, saturable rate bounds, boundary-scaled information, topology-correlated noise in high-complexity quantum devices (P-5 — near-term and accessible), and a gravitating uncomputed sector (P-4). If the universe is not a lazy functional program, these signatures should eventually say so.

The deepest shift, though, is grammatical. Physics has always asked *what exists*. The functional universe answers: nothing exists; everything *happens* — and what happens is a function, applied, deferred, shared, and finally, somewhere within itself, demanded.

---

## Appendix A: Proofs Omitted from the Main Text

**A.1 Type preservation (Theorem 2.2, part 1).** By induction on the derivation of $\Gamma \vdash t : \tau$. Cases: ($\beta$) needs the substitution lemma — if $\Gamma, x:\sigma \vdash t : \tau$ and $\Gamma \vdash u : \sigma$ then $\Gamma \vdash t[u/x] : \tau$ — proved by induction on the first derivation; ($\delta$) is immediate since both sides have type $\mathsf{E}$; ($\mathbf{let}$) is a special case of substitution. $\blacksquare$

**A.2 Progress (Theorem 2.2, part 2).** By induction on typing: a closed well-typed term of arrow type that is not a value is an application whose head is either an abstraction ($\beta$-redex), an atom applied to a value ($\delta$-redex), or a $\mathbf{let}$ ($\mathbf{let}$-redex). $\blacksquare$

**A.3 Confluence (Theorem 2.6), details.** Define parallel reduction $\Rightarrow$ in the standard Tait–Martin-Löf style (all redexes contracted simultaneously), prove the diamond property $t \Rightarrow u, t \Rightarrow v \Rightarrow \exists w: u \Rightarrow w, v \Rightarrow w$ by induction on term structure — the only new cases versus the classical proof are $\delta$, which commutes with everything because (i) $\delta$ redexes are never created or destroyed by $\beta/\mathbf{let}$ on other branches (atoms applied to distinct chains; the rule set has no critical pairs — no left-hand side overlaps another), and (ii) $\mathbf{let}$-substitution of a thunk copies the redex *unevaluated*, preserving joinability via the shared-memo discipline (copies are joined by evaluating the memo once). Confluence of $\to^*$ follows from the diamond of $\Rightarrow$ by the standard tiling argument. $\blacksquare$

**A.4 Strong normalization (Theorem 2.7), details.** Tait reducibility: define $\mathrm{Red}_{\mathsf{E}} = \{$SN terms$\}$, $\mathrm{Red}_{\sigma\to\tau} = \{t : \forall u \in \mathrm{Red}_\sigma,\; t\,u \in \mathrm{Red}_\tau\}$; prove the three standard properties (CR1–CR3: reducible implies SN; neutral terms with reducible reducts are reducible; reducibles contain variables). $\delta$ steps preserve SN since they strictly decrease the number of pending atoms on a chain and atoms are finitely many per finite term; $\mathbf{let}$ unfolds at most the number of distinct bindings under call-by-need. Every well-typed term is reducible by induction on typing, hence SN. $\blacksquare$

**A.5 Theorem 6.9 (stationary phase), details.** Let $H = H(q_i, q_f)$, write $\mathrm{cost} = \gamma + \Delta$ with $\Delta \ge 0$ integer. The sum $Z = \sum_{\mathfrak h} e^{i(\gamma + \Delta_{\mathfrak h})} = e^{i\gamma}\sum_{\Delta} N(\Delta) e^{i\Delta}$ where $N(\Delta)$ counts histories of excess cost $\Delta$. Since $e^{i\Delta}$ for integer $\Delta$ are roots-of-unity-like oscillators and $N(\Delta)$ grows at most polynomially in the regimes considered (finite terms, P6), the phases $\Delta = 1, 2, \dots$ cancel against each other up to $O(1/\Delta_{\max})$ residuals, leaving the $\Delta = 0$ (stationary/minimal) sector dominant; formalizing $N(\Delta)$'s regularity is the continuum-limit task of OP-1. $\blacksquare$

## Appendix B: A Worked Micro-Universe

Let $\Sigma = \{\alpha, \beta\}$, with $\delta$-rules $\alpha\,\langle h\rangle \to \langle \alpha :: h\rangle$ and $\beta\,\langle h\rangle \to \langle \beta :: h\rangle$. Define the two-element universe:

$$
\mathcal{U}_2 \;=\; \mathbf{let}\; e = (\lambda x.\, \alpha x)\;\mathbf{in}\;\; \mathbf{let}\; p = (\lambda y.\, \beta (e\, y))\;\mathbf{in}\;\; p\, \bullet
$$

Evaluation (any strategy): $p\,\bullet \to \beta(e\,\bullet) \to \beta(\alpha\,\bullet) \to \langle\beta :: \alpha :: \cdot\rangle$. Two $\delta$-steps, cost $2$, energy $2\hbar f_\sigma$, unique normal form for all observers (Theorem 5.2 verified by inspection). Now add deferral:

$$
\mathcal{U}_2' \;=\; \mathbf{let}\; d = (\lambda z.\, \alpha (\beta z))\,\bullet \;\mathbf{in}\;\; (\lambda w.\, w)\, \bullet
$$

The thunk $d$ is never demanded: no $\delta$ fires, cost $= 1$ (the single administrative $\beta$), normal form $\bullet$. By Section 9.3, $d$ nonetheless contributes to $\kappa$: the term carries an unforced promise. The micro-universe $\mathcal{U}_2'$ is the simplest model in which *thunk gravity* (P-4) is visible: identical event content to $\bullet$, nonzero structural weight. Finally, share a thunk between two sites:

$$
\mathcal{U}_2'' \;=\; \mathbf{let}\; s = \alpha\,\bullet\;\mathbf{in}\;\; \mathbf{pair}\, (\lambda q.\, q s)\, (\lambda r.\, r s)
$$

Forcing either occurrence of $s$ yields $\langle\alpha\rangle$ for both (Theorem 8.6): the toy universe already contains entanglement. A three-line evaluator for $\mathcal{U}_2$, $\mathcal{U}_2'$, $\mathcal{U}_2''$ in any lazy language reproduces all claimed behaviors and is the seed of the simulation program of OP-6.

---

## References

1. Church, A. (1936). An unsolvable problem of elementary number theory. *American Journal of Mathematics*, 58(2), 345–363.
2. Church, A., & Rosser, J. B. (1936). Some properties of conversion. *Transactions of the American Mathematical Society*, 39(3), 472–482.
3. Noether, E. (1918). Invariante Variationsprobleme. *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse*, 235–257.
4. Feynman, R. P., & Hibbs, A. R. (1965). *Quantum Mechanics and Path Integrals*. McGraw-Hill.
5. Tait, W. W. (1967). Intensional interpretations of functionals of finite type I. *Journal of Symbolic Logic*, 32(2), 198–212.
6. Wheeler, J. A. (1990). Information, physics, quantum: The search for links. In W. Zurek (Ed.), *Complexity, Entropy, and the Physics of Information*. Addison-Wesley.
7. Girard, J.-Y. (1987). Linear logic. *Theoretical Computer Science*, 50(1), 1–101.
8. Atiyah, M. (1988). Topological quantum field theories. *Publications Mathématiques de l'IHÉS*, 68, 175–186.
9. Milner, R. (1996). Calculi for interaction. *Acta Informatica*, 33(8), 707–737.
10. Launchbury, J. (1993). A natural semantics for lazy evaluation. *Proceedings of POPL '93*, 144–154.
11. Margolus, N., & Levitin, L. B. (1998). The maximum speed of dynamical evolution. *Physica D*, 120(1–2), 188–195.
12. Bekenstein, J. D. (1981). Universal upper bound on the entropy-to-energy ratio for bounded systems. *Physical Review D*, 23(2), 287–298.
13. Lloyd, S. (2000). Ultimate physical limits to computation. *Nature*, 406, 1047–1054.
14. Wolfram, S. (2020). *A Project to Find the Fundamental Theory of Physics*. Wolfram Media.
15. 't Hooft, G. (2016). *The Cellular Automaton Interpretation of Quantum Mechanics*. Springer.
16. Lambek, J., & Scott, P. J. (1986). *Introduction to Higher Order Categorical Logic*. Cambridge University Press.

---

*Draft ends. Sections marked Conjecture or Open Problem are invitations, not conclusions.*
