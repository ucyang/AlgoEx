import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())

distance_matrix = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    distance_matrix[i][i] = 0

for _ in range(M):
    start, end, cost = map(int, input().split())
    distance_matrix[start][end] = min(distance_matrix[start][end], cost)

start, end = map(int, input().split())
queue = deque([i for i, cost in enumerate(distance_matrix[start][1:], 1)
               if cost < int(1e9)])

while queue:
    v1 = queue.popleft()
    for v2, cost in enumerate(distance_matrix[v1][1:], 1):
        if distance_matrix[start][v1] + cost < distance_matrix[start][v2]:
            distance_matrix[start][v2] = distance_matrix[start][v1] + cost
            queue.append(v2)

print(distance_matrix[start][end])
