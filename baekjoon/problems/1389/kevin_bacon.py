import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
d = [[0 if i == j else float("inf") for i in range(N)] for j in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    d[i - 1][j - 1] = d[j - 1][i - 1] = 1

for m in range(N):
    for s in range(N):
        for e in range(N):
            if (d[s][e] > d[s][m] + d[m][e]):
                d[s][e] = d[s][m] + d[m][e]

s = [sum(r) for r in d]
print(min(range(len(s)), key=s.__getitem__) + 1)