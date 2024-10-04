import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[[-1] * 3 for _ in range(N)] for _ in range(N)]


def dfs(r, c, d):
    if dp[r][c][d] != -1:
        return dp[r][c][d]

    if ((r == N - 1 and c == N - 2 and d == 0)
        or (r == N - 2 and c == N - 1 and d == 1)
        or (r == N - 2 and c == N - 2 and d == 2)):
        count = 1
    else:
        count = 0

        # Horizontal
        if d == 0:
            if c + 2 < N and matrix[r][c + 2] == 0:
                count += dfs(r, c + 1, 0)
            if (r + 1 < N and c + 2 < N
                and matrix[r][c + 2] == 0
                and matrix[r + 1][c + 1] == 0
                and matrix[r + 1][c + 2] == 0):
                count += dfs(r, c + 1, 2)
        # Vertical
        elif d == 1:
            if r + 2 < N and matrix[r + 2][c] == 0:
                count += dfs(r + 1, c, 1)
            if (r + 2 < N and c + 1 < N
                and matrix[r + 1][c + 1] == 0
                and matrix[r + 2][c] == 0
                and matrix[r + 2][c + 1] == 0):
                count += dfs(r + 1, c, 2)
        # Diagonal
        else:
            if c + 2 < N and matrix[r + 1][c + 2] == 0:
                count += dfs(r + 1, c + 1, 0)
            if r + 2 < N and matrix[r + 2][c + 1] == 0:
                count += dfs(r + 1, c + 1, 1)
            if (r + 2 < N and c + 2 < N
                and matrix[r + 1][c + 2] == 0
                and matrix[r + 2][c + 1] == 0
                and matrix[r + 2][c + 2] == 0):
                count += dfs(r + 1, c + 1, 2)

    dp[r][c][d] = count

    return count


print(dfs(0, 0, 0))
