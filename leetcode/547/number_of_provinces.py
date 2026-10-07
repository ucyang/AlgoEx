class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        cities = set(range(n))
        num_provinces = 0

        while cities:
            city = cities.pop()
            queue = [city]

            while queue:
                i = queue.pop()

                for j in range(n):
                    if isConnected[i][j] and j in cities:
                        cities.remove(j)
                        queue.append(j)

            num_provinces += 1

        return num_provinces
