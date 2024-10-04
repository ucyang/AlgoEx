import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

houses = []
stores = []

for i in range(N):
    row = map(int, input().split())
    for j, v in enumerate(row):
        if v == 1:
            houses.append((i, j))
        elif v == 2:
            stores.append((i, j))

distance = [[0] * len(stores) for _ in range(len(houses))]

for i, (hr, hc) in enumerate(houses):
    for j, (sr, sc) in enumerate(stores):
        distance[i][j] = abs(hr - sr) + abs(hc - sc)

min_distance = 1e9

for stores_indices in combinations(range(len(stores)), M):
    sum_distance = 0
    for i in range(len(houses)):
        sum_distance += min(distance[i][j] for j in stores_indices)
    if sum_distance < min_distance:
        min_distance = sum_distance

print(min_distance)
