"""
Autonomous Agent Normalized Compression Distance (NCD) Skill
Pure Python Standard Library implementation.
"""
import zlib
from typing import List, Dict, Any

class NCDCalculator:
    """
    Universal clustering & semantic distance metric using Normalized Compression Distance.
    NCD(x, y) = (C(xy) - min(C(x), C(y))) / max(C(x), C(y))
    """
    @staticmethod
    def distance(s1: str, s2: str, level: int = 9) -> float:
        b1 = s1.encode("utf-8")
        b2 = s2.encode("utf-8")
        c1 = len(zlib.compress(b1, level))
        c2 = len(zlib.compress(b2, level))
        c12 = len(zlib.compress(b1 + b2, level))
        
        max_c = max(c1, c2)
        if max_c == 0:
            return 0.0
        dist = (c12 - min(c1, c2)) / max_c
        return round(max(0.0, min(1.0, dist)), 4)

    @staticmethod
    def distance_matrix(items: List[str], labels: List[str] = None) -> Dict[str, Any]:
        n = len(items)
        labels = labels or [f"item_{i}" for i in range(n)]
        matrix = [[0.0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                d = NCDCalculator.distance(items[i], items[j])
                matrix[i][j] = d
                matrix[j][i] = d

        return {
            "labels": labels,
            "matrix": matrix
        }
