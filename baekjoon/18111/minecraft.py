import sys

input = lambda: sys.stdin.readline().rstrip()

N, _, B = map(int, input().split())
a = []
for _ in range(N):
    a += map(int, input().split())

min_t = -1
for h in range(min(a), max(a) + 1):
    b, t = B, 0
    for v in a:
        b += v - h
        t += 2 * (v - h) if v > h else h - v
    if b < 0:
        break
    if min_t < 0 or t <= min_t:
        min_t = t
        max_h = h

print(min_t, max_h)