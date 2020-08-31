import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

M, N = map(int, input().split())
l = []
mature = deque()
for y in range(N):
    l.append(list(map(int, input().split())))
    for x in range(M):
        if l[y][x] == 1:
            mature.append((x, y))

while mature:
    x, y = mature.popleft()
    for p in ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)):
        x2, y2 = p
        if 0 <= x2 < M and 0 <= y2 < N and l[y2][x2] == 0:
            l[y2][x2] = l[y][x] + 1
            mature.append(p)

print(-1 if any(0 in l2 for l2 in l) else max(map(max, l)) - 1)