import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

M = 100001
d = [-1] * M
d[N] = 0
q = [N]
while q:
    i = q.pop(0)
    if i == K:
        break
    t = d[i] + 1
    for j in (i - 1, i + 1, 2 * i):
        if 0 <= j < M and (d[j] == -1 or d[j] > t):
            d[j] = t
            q.append(j)
print(d[K])