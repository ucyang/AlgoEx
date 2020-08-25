import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
g = {i: set() for i in range(1, N + 1)}
for _ in range(M):
    i, j = map(int, input().split())
    g[i].add(j)
    g[j].add(i)

c = 0
s = set(range(1, N + 1))
while s:
    c += 1
    q = {s.pop()}
    while q:
        v = q.pop()
        s.discard(v)
        q.update({u for u in g[v] if u in s and u not in q})
print(c)