import sys

sys.setrecursionlimit(10**9)

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if matrix[i][j] == "I":
            start = (i, j)
            break


def dfs(y, x):
    count = 1 if matrix[y][x] == "P" else 0
    matrix[y][x] = "V"

    for i, j in [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]:
        if 0 <= i < N and 0 <= j < M and matrix[i][j] in ("O", "P"):
            count += dfs(i, j)

    return count


print(dfs(start[0], start[1]) or "TT")
