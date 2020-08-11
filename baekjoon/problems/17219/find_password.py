import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
d = {}
for _ in range(n):
    t = input().split()
    d[t[0]] = t[1]
for _ in range(m):
    print(d[input()])