import sys

input = lambda: sys.stdin.readline().rstrip()

_, M = map(int, input().split())
a = list(map(int, input().split()))

l, u = 0, max(a) - 1
while l < u:
    m = (l + u) // 2 + (l + u) % 2
    s = sum(map(lambda x: max(x - m, 0), a))
    if s < M:
        u = m - 1
    else:
        l = m

print(l)