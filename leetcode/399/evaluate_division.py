class Solution:
    def _dfs(self, graph: dict[str, dict[str, float]], visited: set[str], c: str, d: str) -> float:
        for b in graph[c]:
            if b in visited:
                continue
            if b == d:
                return graph[c][d]

            visited.add(b)
            result = self._dfs(graph, visited, b, d)
            
            if result != -1:
                return graph[c][b] * result
        
        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]

            graph[a][b] = v
            graph[b][a] = 1 / v

        result = []

        for c, d in queries:
            if c not in graph or d not in graph:
                result.append(-1)
            elif c == d:
                result.append(1)
            else:
                visited = {c}
                result.append(self._dfs(graph, visited, c, d))

        return result
