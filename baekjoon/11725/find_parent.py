import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
connected = defaultdict(list)

for _ in range(N - 1):
    i, j = map(int, input().split())
    connected[i].append(j)
    connected[j].append(i)

parents = [0] * (N + 1)

queue = [1]
visited = set()

while queue:
    i = queue.pop()
    visited.add(i)

    for j in connected[i]:
        if j not in visited:
            parents[j] = i
            queue.append(j)

for parent_id in parents[2:]:
    print(parent_id)
