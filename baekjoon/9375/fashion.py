import sys
from operator import mul
from functools import reduce

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    d = {}
    for _ in range(int(input())):
        t = input().split()[1]
        if t in d:
            d[t] += 1
        else:
            d[t] = 2
    print(reduce(mul, d.values(), 1) - 1)