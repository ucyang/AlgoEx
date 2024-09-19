import sys
from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
num = list(map(int, input().split()))

for p in sorted(set(permutations(num, M))):
    print(*p)
