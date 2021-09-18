import sys
from itertools import accumulate

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
l = list(map(int, input().split()))
a = [0] + list(accumulate(l))
for _ in range(M):
    i, j = map(int, input().split())
    print(a[j] - a[i - 1])
