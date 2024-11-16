from itertools import combinations

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

for c in combinations(numbers, M):
    print(*c)
