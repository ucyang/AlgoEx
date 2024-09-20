import sys
from itertools import combinations_with_replacement

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
num = sorted(set(map(int, input().split())))

for p in combinations_with_replacement(num, M):
    print(*p)
