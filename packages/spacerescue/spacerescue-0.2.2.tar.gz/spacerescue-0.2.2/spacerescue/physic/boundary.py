import numpy as np


class Boundary:
    def __init__(self, center: np.ndarray, size: float):
        self.center = center
        self.size = size

    def contains(self, position: np.ndarray) -> bool:
        return self.distance(position) < self.size
    
    def distance(self, position: np.ndarray) -> float:
        return float(np.linalg.norm(self.center - position))
