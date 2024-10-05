class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [y[1] for y in sorted((x[1], x[0]) for x in enumerate(mat))[:k]]
