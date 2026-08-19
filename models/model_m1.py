# models/model_m1.py
"""
M1: Linear/Complex Representation
Extends M0 with complex amplitudes and path summation.
"""
import cmath

class Amplitude:
    def __init__(self, value: complex = 1.0+0j):
        self.value = value

    def __mul__(self, other):
        return Amplitude(self.value * other.value)
        
    def __add__(self, other):
        return Amplitude(self.value + other.value)

class QuantumAction(PureAction):
    """An action that carries a complex amplitude."""
    def __init__(self, name, domain, codomain, func, amp: Amplitude):
        super().__init__(name, domain, codomain, func)
        self.amp = amp

class Universe_M1(Universe_M0):
    def path_sum(self, paths: list) -> complex:
        """K(X_f, X_i) = sum_{paths} Z(path)"""
        total_amp = 0j
        for path in paths:
            path_amp = 1j * 0
            for a in path:
                path_amp *= a.amp.value
            total_amp += path_amp
        return total_amp

    def born_probability(self, amp: complex) -> float:
        """P = |K|^2 (Assumed/effective at this layer)"""
        return abs(amp)**2