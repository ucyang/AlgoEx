from itertools import product

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

for p in product(range(N), repeat=M):
    print(*[numbers[i] for i in p])
