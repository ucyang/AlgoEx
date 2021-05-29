import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
d = {}
for _ in range(N + M):
    i, j = map(int, input().split())
    d[i] = j

s = set()
q = deque([(1, 0)])
while q:
    v, c = q.popleft()
    if v == 100:
        print(c)
        break
    s.add(v)
    for i in range(1, 7):
        u = v + i
        while u in d:
            u = d[u]
        if u not in s:
            q.append((u, c + 1))
            s.add(u)
