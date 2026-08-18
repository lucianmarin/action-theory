# model_m1.py
"""
Model M1: Minimal Finite Action Model for Action Theory / CFR

This implements a small finite action category/graph with:

    (A, circ, C, Z, G)

where:
    A = elementary actions (directed edges)
    circ = path composition
    C = admissibility constraints (disabled actions / path filters)
    Z = multiplicative action amplitudes
    G = simple local gauge rephasing demonstration

Research status:
    - This is a toy model.
    - Complex amplitudes are assumed/effective.
    - Born-like probabilities are assumed/effective.
    - Freedom geometry is represented by continuation rank.
    - Roadblock = vanishing freedom rank / no admissible continuations.

The goal is not to insert QM/GR/SM by hand, but to see whether
action-network primitives can generate interference, constraints,
freedom loss, Roadblocks, and intervention effects.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, replace
from typing import Callable, Dict, Iterable, List, Optional, Set, Tuple

Node = str
Path = Tuple[str, ...]


# ----------------------------------------------------------------------------
# Linear-algebra helper: complex matrix rank without external dependencies
# ----------------------------------------------------------------------------

def matrix_rank(mat: List[List[complex]], tol: float = 1e-10) -> int:
    """
    Compute the rank of a complex matrix using Gaussian elimination.

    This is intentionally simple and suitable for small toy matrices.
    """
    if not mat:
        return 0

    n_rows = len(mat)
    n_cols = len(mat[0])

    if n_cols == 0:
        return 0

    # Copy so we do not mutate the input.
    m = [row[:] for row in mat]

    rank = 0

    for col in range(n_cols):
        # Find pivot.
        pivot = None
        for r in range(rank, n_rows):
            if abs(m[r][col]) > tol:
                pivot = r
                break

        if pivot is None:
            continue

        # Move pivot row into position.
        m[rank], m[pivot] = m[pivot], m[rank]

        # Normalize pivot row.
        pivot_value = m[rank][col]
        for c in range(col, n_cols):
            m[rank][c] /= pivot_value

        # Eliminate this column from all other rows.
        for r in range(n_rows):
            if r == rank:
                continue

            factor = m[r][col]
            if abs(factor) <= tol:
                continue

            for c in range(col, n_cols):
                m[r][c] -= factor * m[rank][c]

        rank += 1

        if rank == n_rows:
            break

    return rank


# ----------------------------------------------------------------------------
# Elementary action
# ----------------------------------------------------------------------------

@dataclass(frozen=True)
class Action:
    """
    An elementary action is a directed transition between action-nodes.

    The nodes are not assumed to be spacetime points. They are boundary
    conditions / partial-history labels / action configurations.
    """
    name: str
    src: Node
    dst: Node
    weight: complex = 1.0 + 0.0j


# ----------------------------------------------------------------------------
# Finite action model
# ----------------------------------------------------------------------------

class FiniteActionModel:
    """
    A finite action model:

        (A, circ, C, Z, G)

    The composition rule circ is path concatenation.
    Constraints C are represented by disabled actions and optional
    path_constraint(path) -> bool.
    Amplitudes Z are multiplicative edge weights.
    Gauge G is demonstrated by local rephasing of edge weights.
    """

    def __init__(
        self,
        actions: Iterable[Action],
        disabled: Optional[Set[str]] = None,
        path_constraint: Optional[Callable[[Path], bool]] = None,
    ) -> None:
        self.actions: Dict[str, Action] = {a.name: a for a in actions}
        self.disabled: Set[str] = set(disabled) if disabled is not None else set()
        self.path_constraint = path_constraint

    # ------------------------------------------------------------------
    # Basic structural tools
    # ------------------------------------------------------------------

    def nodes(self) -> List[Node]:
        """All nodes appearing in the action graph."""
        node_set: Set[Node] = set()
        for a in self.actions.values():
            node_set.add(a.src)
            node_set.add(a.dst)
        return sorted(node_set)

    def outgoing(self, node: Node) -> List[Action]:
        """Allowed outgoing elementary actions from a node."""
        result = []
        for a in self.actions.values():
            if a.src == node and a.name not in self.disabled:
                result.append(a)
        return sorted(result, key=lambda x: x.name)

    def is_action_allowed(self, name: str) -> bool:
        """An elementary action is allowed if it exists and is not disabled."""
        return name in self.actions and name not in self.disabled

    def path_allowed(self, path: Path) -> bool:
        """
        A path is admissible if every action is allowed and the optional
        global path_constraint accepts it.
        """
        for name in path:
            if not self.is_action_allowed(name):
                return False

        if self.path_constraint is not None:
            if not self.path_constraint(path):
                return False

        return True

    def with_disabled(self, extra_disabled: Iterable[str]) -> "FiniteActionModel":
        """
        Return a new model with additional actions disabled.
        This is used to model interventions/constraints.
        """
        return FiniteActionModel(
            actions=self.actions.values(),
            disabled=self.disabled.union(set(extra_disabled)),
            path_constraint=self.path_constraint,
        )

    # ------------------------------------------------------------------
    # Paths, composition, amplitudes
    # ------------------------------------------------------------------

    def path_weight(self, path: Path) -> complex:
        """
        Multiplicative amplitude of a path:

            Z(path) = product_a Z(a)

        If any action is disallowed, the amplitude is zero.
        """
        w = 1.0 + 0.0j

        for name in path:
            if not self.is_action_allowed(name):
                return 0.0 + 0.0j
            w *= self.actions[name].weight

        return w

    def endpoint_after_path(self, start: Node, path: Path) -> Optional[Node]:
        """
        Given a starting node and a path, return the endpoint.
        If the path is not composable from start, return None.
        """
        node = start

        for name in path:
            if not self.is_action_allowed(name):
                return None

            action = self.actions[name]

            if action.src != node:
                return None

            node = action.dst

        return node

    def iter_paths(
        self,
        start: Node,
        end: Optional[Node] = None,
        max_depth: int = 4,
        min_depth: int = 0,
    ) -> Iterable[Path]:
        """
        Enumerate admissible paths from start up to max_depth.

        If end is given, only paths ending at that node are yielded.
        If end is None, all paths are yielded.

        min_depth controls whether the empty path is allowed.
        """
        stack: List[Tuple[Node, Path]] = [(start, tuple())]

        while stack:
            node, path = stack.pop()

            if len(path) >= min_depth:
                if end is None or node == end:
                    yield path

            if len(path) >= max_depth:
                continue

            for action in self.outgoing(node):
                new_path = path + (action.name,)

                if self.path_allowed(new_path):
                    stack.append((action.dst, new_path))

    def transition_amplitude(
        self,
        src: Node,
        dst: Node,
        max_depth: int = 4,
    ) -> complex:
        """
        CFR finite path-sum amplitude:

            K(dst, src) = sum_{paths src -> dst} Z(path)

        The empty path contributes 1 if src == dst.
        """
        total = 0.0 + 0.0j

        for path in self.iter_paths(
            start=src,
            end=dst,
            max_depth=max_depth,
            min_depth=0,
        ):
            total += self.path_weight(path)

        return total

    def transition_probability(
        self,
        src: Node,
        dst: Node,
        max_depth: int = 4,
    ) -> float:
        """
        Born-like probability, currently assumed/effective:

            P = |K|^2
        """
        amp = self.transition_amplitude(src, dst, max_depth=max_depth)
        return abs(amp) ** 2

    # ------------------------------------------------------------------
    # Freedom geometry, rank, Roadblocks
    # ------------------------------------------------------------------

    def continuations(self, node: Node, max_depth: int = 3) -> List[Path]:
        """
        Admissible continuations from a node.

        These are the finite-model analog of N(h), where h ends at node.
        We exclude the empty path because freedom concerns future
        continuations, not standing still.
        """
        return list(
            self.iter_paths(
                start=node,
                end=None,
                max_depth=max_depth,
                min_depth=1,
            )
        )

    def freedom(
        self,
        node: Node,
        max_depth: int = 3,
        mode: str = "path",
        tol: float = 1e-12,
    ) -> Dict[str, float]:
        """
        Compute a simple freedom measure for a node/history endpoint.

        mode = "path":
            Each admissible continuation path is treated as an independent
            basis direction. This is crude but useful for first tests.

        mode = "endpoint":
            Continuations are represented by their endpoint only.
            This coarse-grains different paths to the same endpoint.

        Returns:
            n_continuations: number of nonzero-amplitude continuations
            rank: rank of continuation matrix
            volume: crude freedom volume, product of continuation amplitudes
            roadblock: True if rank == 0
        """
        cont = self.continuations(node, max_depth=max_depth)

        rows: List[List[complex]] = []
        amps: List[complex] = []

        if mode == "path":
            # First collect nonzero-amplitude continuations.
            nonzero_paths: List[Path] = []

            for p in cont:
                amp = self.path_weight(p)
                if abs(amp) > tol:
                    nonzero_paths.append(p)
                    amps.append(amp)

            # Path-one-hot feature representation.
            # Row i has amplitude amp_i in column i.
            n = len(nonzero_paths)
            for i, amp in enumerate(amps):
                row = [0.0 + 0.0j] * n
                row[i] = amp
                rows.append(row)

        elif mode == "endpoint":
            nodes = self.nodes()
            node_index = {n: i for i, n in enumerate(nodes)}

            for p in cont:
                amp = self.path_weight(p)
                if abs(amp) <= tol:
                    continue

                ep = self.endpoint_after_path(node, p)
                if ep is None:
                    continue

                row = [0.0 + 0.0j] * len(nodes)
                row[node_index[ep]] = amp

                rows.append(row)
                amps.append(amp)

        else:
            raise ValueError("mode must be 'path' or 'endpoint'")

        rank = matrix_rank(rows, tol=tol)

        # Very crude freedom volume.
        # In a more serious model this should come from det(G) or
        # a gauge-invariant volume on continuation space.
        if amps:
            log_volume = 0.0
            for a in amps:
                mag = abs(a)
                if mag > 1e-300:
                    log_volume += math.log(mag)

            if log_volume > 700:
                volume = float("inf")
            else:
                volume = math.exp(log_volume)
        else:
            volume = 0.0

        return {
            "node": node,
            "mode": mode,
            "max_depth": max_depth,
            "n_continuations": len(amps),
            "rank": float(rank),
            "volume": volume,
            "roadblock": rank == 0,
        }

    # ------------------------------------------------------------------
    # Simple future-signature for state-equivalence experiments
    # ------------------------------------------------------------------

    def future_signature(
        self,
        node: Node,
        max_depth: int = 3,
        tol: float = 1e-12,
    ) -> Tuple[Tuple[str, float], ...]:
        """
        A crude signature of future possibilities.

        This is not a full CFR state-equivalence test, but it is useful
        for comparing nodes in the toy model.

        It records endpoint + absolute amplitude for each continuation.
        Phases are ignored here, because phase significance depends on
        larger compositional context.
        """
        cont = self.continuations(node, max_depth=max_depth)
        signature: List[Tuple[str, float]] = []

        for p in cont:
            amp = self.path_weight(p)
            if abs(amp) <= tol:
                continue

            ep = self.endpoint_after_path(node, p)
            if ep is None:
                continue

            signature.append((ep, round(abs(amp), 12)))

        return tuple(sorted(signature))


# ----------------------------------------------------------------------------
# Gauge transformation demonstration
# ----------------------------------------------------------------------------

def gauge_transform(
    model: FiniteActionModel,
    phases: Dict[Node, float],
) -> FiniteActionModel:
    """
    Local U(1)-style rephasing:

        U_xy -> exp(i theta_x) U_xy exp(-i theta_y)

    For fixed boundary nodes, |K(dst, src)| should be unchanged.
    This is an assumed gauge redundancy in Model M1, not yet derived.
    """
    new_actions: List[Action] = []

    for a in model.actions.values():
        theta_src = phases.get(a.src, 0.0)
        theta_dst = phases.get(a.dst, 0.0)

        phase = theta_src - theta_dst
        new_weight = a.weight * cmath.exp(1j * phase)

        new_actions.append(replace(a, weight=new_weight))

    return FiniteActionModel(
        actions=new_actions,
        disabled=model.disabled,
        path_constraint=model.path_constraint,
    )


# ----------------------------------------------------------------------------
# Intervention / influence test
# ----------------------------------------------------------------------------

def intervention_effect(
    model: FiniteActionModel,
    src: Node,
    dst: Node,
    intervention_disabled: Iterable[str],
    max_depth: int = 4,
    tol: float = 1e-12,
) -> Dict[str, float]:
    """
    Test whether disabling actions in region A changes probabilities at B.

    This implements the finite-model version of:

        A affects B iff P_B after intervention != P_B before intervention.
    """
    p_before = model.transition_probability(src, dst, max_depth=max_depth)

    intervened = model.with_disabled(intervention_disabled)
    p_after = intervened.transition_probability(src, dst, max_depth=max_depth)

    delta = p_after - p_before

    return {
        "p_before": p_before,
        "p_after": p_after,
        "delta": delta,
        "effect": abs(delta) > tol,
    }


# ----------------------------------------------------------------------------
# Optional: simple entanglement nonfactorizability check
# ----------------------------------------------------------------------------

def amplitude_matrix_rank(matrix: List[List[complex]], tol: float = 1e-10) -> int:
    """
    Rank of a 2-subsystem amplitude matrix C_ij.

    If rank(C) == 1, the amplitude matrix factorizes.
    If rank(C) > 1, it is nonfactorizable and therefore entangled
    in the effective Hilbert-space representation.
    """
    return matrix_rank(matrix, tol=tol)


def demo_entanglement() -> None:
    """
    Demonstrate nonfactorizability using effective amplitude matrices.

    This is not yet derived from the finite action graph; it is an
    optional check showing what CFR means by entanglement as
    nonfactorizability of action possibilities.
    """
    print("\n=== Optional entanglement check ===")

    # Product-like amplitude matrix:
    # C_ij = a_i b_j, rank 1.
    product_matrix = [
        [1.0 + 0.0j, 1.0 + 0.0j],
        [1.0 + 0.0j, 1.0 + 0.0j],
    ]

    # Bell-like unnormalized amplitude matrix:
    # |00> + |11>, rank 2, nonfactorizable.
    bell_like_matrix = [
        [1.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 1.0 + 0.0j],
    ]

    r_product = amplitude_matrix_rank(product_matrix)
    r_bell = amplitude_matrix_rank(bell_like_matrix)

    print(f"product matrix rank = {r_product}")
    print(f"bell-like matrix rank = {r_bell}")

    print("product matrix factorizable?", r_product <= 1)
    print("bell-like matrix nonfactorizable?", r_bell > 1)


# ----------------------------------------------------------------------------
# Main Model M1 demonstration
# ----------------------------------------------------------------------------

def build_model_m1(theta: float = math.pi / 3) -> FiniteActionModel:
    """
    Build the minimal two-path action graph:

        i -> a -> f
        i -> b -> f

    plus one isolated action x -> y to test irrelevant interventions.

    The two paths interfere at f.
    """
    actions = [
        # Upper path
        Action(name="i->a", src="i", dst="a", weight=1.0 + 0.0j),
        Action(name="a->f", src="a", dst="f", weight=1.0 + 0.0j),

        # Lower path
        Action(name="i->b", src="i", dst="b", weight=1.0 + 0.0j),
        Action(
            name="b->f",
            src="b",
            dst="f",
            weight=cmath.exp(1j * theta),
        ),

        # Isolated action, irrelevant to i -> f
        Action(name="x->y", src="x", dst="y", weight=1.0 + 0.0j),
    ]

    return FiniteActionModel(actions)


def demo() -> None:
    theta = math.pi / 3
    model = build_model_m1(theta=theta)

    print("=== Model M1: Minimal Finite Action Model ===")
    print(f"Lower-path phase theta = {theta:.6f} rad")
    print(f"Expected interference probability = 2 + 2 cos(theta) = {2 + 2 * math.cos(theta):.6f}")

    # ------------------------------------------------------------------
    # 1. Transition amplitude and interference
    # ------------------------------------------------------------------
    print("\n--- 1. Transition amplitude / interference ---")

    K = model.transition_amplitude("i", "f", max_depth=3)
    P = model.transition_probability("i", "f", max_depth=3)

    print(f"K(i -> f) = {K}")
    print(f"P(i -> f) = {P:.6f}")

    # ------------------------------------------------------------------
    # 2. Constraint: disable lower path
    # ------------------------------------------------------------------
    print("\n--- 2. Constraint: disable lower path ---")

    constrained = model.with_disabled({"i->b"})

    K_constrained = constrained.transition_amplitude("i", "f", max_depth=3)
    P_constrained = constrained.transition_probability("i", "f", max_depth=3)

    print(f"K after disabling i->b = {K_constrained}")
    print(f"P after disabling i->b = {P_constrained:.6f}")

    # ------------------------------------------------------------------
    # 3. Freedom and Roadblock at i
    # ------------------------------------------------------------------
    print("\n--- 3. Freedom and Roadblock at i ---")

    free_full = model.freedom("i", max_depth=2, mode="path")
    print("Freedom at i, full model:")
    print(f"    continuations = {free_full['n_continuations']}")
    print(f"    rank          = {free_full['rank']}")
    print(f"    volume        = {free_full['volume']}")
    print(f"    roadblock     = {free_full['roadblock']}")

    constrained_1 = model.with_disabled({"i->b"})
    free_one_path = constrained_1.freedom("i", max_depth=2, mode="path")

    print("\nFreedom at i after disabling lower path:")
    print(f"    continuations = {free_one_path['n_continuations']}")
    print(f"    rank          = {free_one_path['rank']}")
    print(f"    volume        = {free_one_path['volume']}")
    print(f"    roadblock     = {free_one_path['roadblock']}")

    constrained_all = model.with_disabled({"i->a", "i->b"})
    free_none = constrained_all.freedom("i", max_depth=2, mode="path")

    print("\nFreedom at i after disabling both outgoing paths:")
    print(f"    continuations = {free_none['n_continuations']}")
    print(f"    rank          = {free_none['rank']}")
    print(f"    volume        = {free_none['volume']}")
    print(f"    roadblock     = {free_none['roadblock']}")

    # ------------------------------------------------------------------
    # 4. Roadblock at terminal node f
    # ------------------------------------------------------------------
    print("\n--- 4. Roadblock at terminal node f ---")

    free_f = model.freedom("f", max_depth=2, mode="path")
    print("Freedom at f:")
    print(f"    continuations = {free_f['n_continuations']}")
    print(f"    rank          = {free_f['rank']}")
    print(f"    roadblock     = {free_f['roadblock']}")

    # ------------------------------------------------------------------
    # 5. Intervention effect: A -> B
    # ------------------------------------------------------------------
    print("\n--- 5. Intervention effect: A -> B ---")

    # Intervention at A = disable lower path action i->b.
    # Target B = transition probability i -> f.
    effect_relevant = intervention_effect(
        model=model,
        src="i",
        dst="f",
        intervention_disabled={"i->b"},
        max_depth=3,
    )

    print("Intervention: disable i->b")
    print(f"    P before = {effect_relevant['p_before']:.6f}")
    print(f"    P after  = {effect_relevant['p_after']:.6f}")
    print(f"    delta    = {effect_relevant['delta']:.6f}")
    print(f"    effect?  = {effect_relevant['effect']}")

    # Irrelevant intervention: disable isolated x->y.
    effect_irrelevant = intervention_effect(
        model=model,
        src="i",
        dst="f",
        intervention_disabled={"x->y"},
        max_depth=3,
    )

    print("\nIntervention: disable isolated x->y")
    print(f"    P before = {effect_irrelevant['p_before']:.6f}")
    print(f"    P after  = {effect_irrelevant['p_after']:.6f}")
    print(f"    delta    = {effect_irrelevant['delta']:.6f}")
    print(f"    effect?  = {effect_irrelevant['effect']}")

    # ------------------------------------------------------------------
    # 6. Gauge invariance check
    # ------------------------------------------------------------------
    print("\n--- 6. Gauge invariance check ---")

    phases = {
        "i": 0.31,
        "a": 1.17,
        "b": -0.42,
        "f": 0.89,
        "x": 0.05,
        "y": -1.20,
    }

    gauge_model = gauge_transform(model, phases)

    K_original = model.transition_amplitude("i", "f", max_depth=3)
    K_gauge = gauge_model.transition_amplitude("i", "f", max_depth=3)

    print(f"Original K       = {K_original}")
    print(f"Gauge-transformed K = {K_gauge}")

    print(f"|K| original = {abs(K_original):.12f}")
    print(f"|K| gauge    = {abs(K_gauge):.12f}")

    print("Probability invariant under local rephasing?",
          abs(abs(K_original) ** 2 - abs(K_gauge) ** 2) < 1e-12)

    # ------------------------------------------------------------------
    # 7. Optional entanglement check
    # ------------------------------------------------------------------
    demo_entanglement()

    print("\n=== Model M1 run complete ===")


if __name__ == "__main__":
    demo()