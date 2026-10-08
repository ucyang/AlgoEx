class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        tree = [{} for _ in range(n)]

        for a, b in connections:
            tree[a][b] = 1
            tree[b][a] = 0

        queue = [(0, -1)]
        count = 0

        while queue:
            a, p = queue.pop()
    
            for b, d in tree[a].items():
                if b != p:
                    queue.append((b, a))
                    count += d
    
        return count
