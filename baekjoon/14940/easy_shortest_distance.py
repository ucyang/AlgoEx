import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            goal = (i, j)
            # matrix[i][j] = 2
            break

path_queue = deque([(goal[0], goal[1])])

while path_queue:
    y, x = path_queue.popleft()

    for i, j in [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]:
        if (0 <= i < n and 0 <= j < m
            and matrix[i][j] == 1):
            matrix[i][j] = matrix[y][x] + 1
            path_queue.append((i, j))

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            matrix[i][j] = -1
        elif matrix[i][j]:
            matrix[i][j] -= 2

for r in matrix:
    print(*r, sep=" ")
