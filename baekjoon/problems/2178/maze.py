import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]

q = deque([(0, 0, 1)])
while q:
    x, y, c = q.popleft()
    if x == M - 1 and y == N - 1:
        print(c)
        break
    if 0 <= x < M and 0 <= y < N and A[y][x]:
        A[y][x] = 0
        c += 1
        q += [(x - 1, y, c), (x, y - 1, c), (x + 1, y, c), (x, y + 1, c)]