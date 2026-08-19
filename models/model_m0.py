# models/model_m0.py
"""
M0: Pure Action Calculus
Implements the foundational layer of Action Theory.
No spacetime, amplitudes, or mutable state.
Only pure values, typed actions, composition, constraints, and histories.
"""
from typing import Any, List, Set, Tuple, Callable

class Value:
    """Immutable data representing an action boundary or partial history."""
    def __init__(self, data: Any):
        self.data = data

class PureAction:
    """A typed transformation between values. No side effects."""
    def __init__(self, name: str, domain: type, codomain: type, func: Callable):
        self.name = name
        self.domain = domain
        self.codomain = codomain
        self.func = func

    def apply(self, val: Value) -> Value:
        return Value(self.func(val.data))

class History:
    """Immutable composition of pure actions."""
    def __init__(self, initial_val: Value, actions: List[PureAction]):
        self.initial_val = initial_val
        self.actions = tuple(actions)
        self.current_val = initial_val
        for a in self.actions:
            self.current_val = a.apply(self.current_val)

    def compose(self, action: PureAction) -> 'History':
        if type(self.current_val) != action.domain:
            raise ValueError("Constraint violation: action domain mismatch")
        return History(self.initial_val, list(self.actions) + [action])

    def __eq__(self, other):
        """Observational equivalence: two histories are the same state
        if they yield identical admissible future continuations."""
        return self.current_val.data == other.current_val.data

class Constraint:
    """Restricts the set of admissible continuations N(h)."""
    def __init__(self, predicate: Callable):
        self.predicate = predicate

    def is_admissible(self, history: History, action: PureAction) -> bool:
        return self.predicate(history, action)

class Universe_M0:
    def __init__(self, constraints: List[Constraint]):
        self.constraints = constraints

    def continuations(self, h: History, available_actions: List[PureAction]) -> List[History]:
        """Returns N(h), the set of admissible future histories."""
        N_h = []
        for a in available_actions:
            if all(c.is_admissible(h, a) for c in self.constraints):
                N_h.append(h.compose(a))
        return N_h

    def is_roadblock(self, h: History, available_actions: List[PureAction]) -> bool:
        """A Roadblock occurs when the freedom channel closes: N(h) = ∅."""
        return len(self.continuations(h, available_actions)) == 0