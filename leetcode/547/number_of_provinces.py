class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = [False] * n
        num_provinces = 0

        for city in range(n):
            if visited[city]:
                continue

            queue = [city]
            visited[city] = True

            while queue:
                i = queue.pop()

                for j in range(n):
                    if isConnected[i][j] and not visited[j]:
                        queue.append(j)
                        visited[j] = True

            num_provinces += 1

        return num_provinces
