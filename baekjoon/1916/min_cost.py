import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())

adj_matrix = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    adj_matrix[i][i] = 0

for _ in range(M):
    start, end, cost = map(int, input().split())
    adj_matrix[start][end] = min(adj_matrix[start][end], cost)

start, end = map(int, input().split())
queue = deque([i for i, cost in enumerate(adj_matrix[start][1:], 1) if cost < int(1e9)])

while queue:
    v1 = queue.popleft()
    for v2, cost in enumerate(adj_matrix[v1][1:], 1):
        if adj_matrix[start][v1] + cost < adj_matrix[start][v2]:
            adj_matrix[start][v2] = adj_matrix[start][v1] + cost
            queue.append(v2)

print(adj_matrix[start][end])
