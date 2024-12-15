import sys

input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


def is_adjacent(i, j):
    return ((i > 0 and visited[i - 1][j])
            or (i < N - 1 and visited[i + 1][j])
            or (j > 0 and visited[i][j - 1])
            or (j < M - 1 and visited[i][j + 1]))


def dfs(start_i, start_j, k):
    max_sum = int(-1e9)

    for i in range(start_i, N):
        for j in range(start_j if i == start_i else 0, M):
            if not is_adjacent(i, j):
                s = matrix[i][j]

                visited[i][j] = True

                if k > 1:
                    s += dfs(i, j + 2, k - 1)

                visited[i][j] = False

                if s > max_sum:
                    max_sum = s

    return max_sum


print(dfs(0, 0, K))
