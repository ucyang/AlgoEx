class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        queue = deque([tuple(entrance)])
        maze[entrance[0]][entrance[1]] = "+"

        m = len(maze)
        n = len(maze[0])

        steps = 1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == ".":
                        if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                            return steps

                        queue.append((nr, nc))
                        maze[nr][nc] = "+"

            steps += 1

        return -1
