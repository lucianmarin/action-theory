# models/model_m2.py
"""
M2: Continuation Geometry
Constructs the mathematical structure for Freedom Geometry G_AB 
and Freedom Volume V_F.
"""
import numpy as np

class FreedomGeometry:
    def __init__(self, continuations: list):
        self.continuations = continuations
        self.G = self._compute_metric()

    def _compute_metric(self) -> np.ndarray:
        """Constructs the Gram matrix G_AB of continuation space."""
        n = len(self.continuations)
        G = np.zeros((n, n))
        # In a full implementation, this derives from inner products 
        # of the action histories in the continuation space.
        for i in range(n):
            for j in range(n):
                G[i, j] = 1.0 if i == j else 0.5 # Toy metric
        return G

    def freedom_volume(self) -> float:
        """V_F = sqrt(|det G|)"""
        det_G = np.linalg.det(self.G)
        if det_G <= 0: return 0.0
        return np.sqrt(det_G)

    def rank(self) -> int:
        """Freedom dimension. Rank change signals new physics."""
        return np.linalg.matrix_rank(self.G)