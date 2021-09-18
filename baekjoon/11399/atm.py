import sys
from itertools import accumulate
from operator import add

input = lambda: sys.stdin.readline().rstrip()

input()
print(sum(accumulate(sorted(map(int, input().split())), add)))