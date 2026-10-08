class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        tree = defaultdict(list)
        rtree = defaultdict(list)

        for a, b in connections:
            tree[b].append(a)
            rtree[a].append(b)

        queue = [0]

        visited = [False] * n
        visited[0] = True

        count = 0

        while queue:
            a = queue.pop()
    
            for b in tree[a]:
                if not visited[b]:
                    queue.append(b)
                    visited[b] = True
    
            for b in rtree[a]:
                if not visited[b]:
                    queue.append(b)
                    visited[b] = True
                    count += 1
    
        return count
