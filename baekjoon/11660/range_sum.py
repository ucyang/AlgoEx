import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
ranges = [list(map(int, input().split())) for _ in range(M)]

for i in range(N):
    s = 0
    for j in range(N):
        s += matrix[i][j]
        if i:
            matrix[i][j] = matrix[i - 1][j] + s
        else:
            matrix[i][j] = s

for x1, y1, x2, y2 in ranges:
    s = matrix[x2 - 1][y2 - 1]
    if x1 > 1:
        s -= matrix[x1 - 2][y2 - 1]
    if y1 > 1:
        s -= matrix[x2 - 1][y1 - 2]
    if x1 > 1 and y1 > 1:
        s += matrix[x1 - 2][y1 - 2]
    print(s)
