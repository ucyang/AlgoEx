import sys

input = lambda: sys.stdin.readline().rstrip()

k, n = map(int, input().split())
a = [int(input()) for _ in range(k)]

l, r = 1, max(a)
while l < r:
    m = (l + r) // 2 + (l + r) % 2
    s = sum(map(lambda x: x // m, a))
    if s < n:
        r = m - 1
    else:
        l = m

print(r)
