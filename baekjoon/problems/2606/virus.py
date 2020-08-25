import sys

input = lambda: sys.stdin.readline().rstrip()

g = {i: set() for i in range(1, int(input()) + 1)}
for _ in range(int(input())):
    i, j = map(int, input().split())
    g[i].add(j)
    g[j].add(i)

prev_s = set()
next_s = {1}
while next_s:
    v = next_s.pop()
    prev_s.add(v)
    for u in g[v]:
        if u not in prev_s:
            next_s.add(u)
print(len(prev_s) - 1)