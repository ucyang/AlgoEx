from itertools import product

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

for p in product(numbers, repeat=M):
    print(*p)
