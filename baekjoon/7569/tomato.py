import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

M, N, H = map(int, input().split())
l = []
mature = deque()
for z in range(H):
    l.append([])
    for y in range(N):
        l[z].append(list(map(int, input().split())))
        for x in range(M):
            if l[z][y][x] == 1:
                mature.append((x, y, z))

while mature:
    x, y, z = mature.popleft()
    for p in ((x - 1, y, z), (x, y - 1, z), (x, y, z - 1),
        (x + 1, y, z), (x, y + 1, z), (x, y, z + 1)):
        x2, y2, z2 = p
        if 0 <= x2 < M and 0 <= y2 < N and 0 <= z2 < H and l[z2][y2][x2] == 0:
            l[z2][y2][x2] = l[z][y][x] + 1
            mature.append(p)

print(-1 if any(any(0 in l3 for l3 in l2) for l2 in l)
    else max(map(max, map(lambda x: map(max, x), l))) - 1)