import sys
from math import isinf

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
d = [list(map(lambda x: int(x) if int(x) else float("inf"), \
    input().split())) for _ in range(N)]

for m in range(N):
    for s in range(N):
        for e in range(N):
            if (d[s][e] > d[s][m] + d[m][e]):
                d[s][e] = d[s][m] + d[m][e]

for r in d:
    print(*map(lambda x: 0 if isinf(x) else 1, r))