import sys

input = lambda: sys.stdin.readline().rstrip()

N, M, V = map(int, input().split())
g = {i: set() for i in range(1, N + 1)}
for _ in range(M):
    i, j = map(int, input().split())
    g[i].add(j)
    g[j].add(i)

def dfs(s, v, ret):
    s.add(v)
    ret.append(v)
    for u in sorted(g[v]):
        if u not in s:
            dfs(s, u, ret)

ret = []
dfs(set(), V, ret)
print(*ret)

ret.clear()
s = set()
q = [V]
while q:
    v = q.pop(0)
    s.add(v)
    q += [u for u in sorted(g[v]) if u not in s and u not in q]
    ret.append(v)
print(*ret)