class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        queue = deque([tuple(entrance)])
        visited = set(tuple(entrance))

        m = len(maze)
        n = len(maze[0])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if (r != entrance[0] or c != entrance[1]) and (
                    r == 0 or r == m - 1 or c == 0 or c == n - 1
                ):
                    return steps

                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (
                        0 <= nr < m
                        and 0 <= nc < n
                        and (nr, nc) not in visited
                        and maze[nr][nc] == "."
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

            steps += 1

        return -1
