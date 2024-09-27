import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
ranges = [list(map(int, input().split())) for _ in range(M)]

for i in range(N):
    for j in range(1, N):
        matrix[i][j] += matrix[i][j - 1]

for x1, y1, x2, y2 in ranges:
    s = 0
    for x in range(x1 - 1, x2):
        if y1 > 1:
            s += matrix[x][y2 - 1] - matrix[x][y1 - 2]
        else:
            s += matrix[x][y2 - 1]
    print(s)
