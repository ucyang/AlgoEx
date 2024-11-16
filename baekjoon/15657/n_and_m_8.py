from itertools import combinations_with_replacement

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

for c in combinations_with_replacement(numbers, M):
    print(*c)
