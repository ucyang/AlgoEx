class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        tree = [[] for _ in range(n)]
        rtree = [[] for _ in range(n)]

        for a, b in connections:
            tree[b].append(a)
            rtree[a].append(b)

        queue = [(0, -1)]
        count = 0

        while queue:
            a, p = queue.pop()
    
            for b in tree[a]:
                if b != p:
                    queue.append((b, a))
    
            for b in rtree[a]:
                if b != p:
                    queue.append((b, a))
                    count += 1
    
        return count
