class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        m = len(grid)
        n = len(grid[0])

        queue = deque()

        num_fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    num_fresh += 1

        if num_fresh == 0:
            return 0

        minutes = -1

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for di, dj in DIRS:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        queue.append((ni, nj))
                        grid[ni][nj] = 2
                        num_fresh -= 1

            minutes += 1

        return minutes if num_fresh == 0 else -1
