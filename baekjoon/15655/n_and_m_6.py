from itertools import combinations

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

for p in combinations(range(N), M):
    print(*[numbers[i] for i in p])
