import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
s = {input() for _ in range(n)}
l = []
for _ in range(m):
    t = input()
    if t in s:
        s.remove(t)
        l.append(t)
l.sort()
print(len(l), *l, sep="\n")