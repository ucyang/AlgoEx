import sys
from operator import itemgetter

input = lambda: sys.stdin.readline().rstrip()

s = 0
c = 0
for t in sorted(
    sorted(tuple(map(int, input().split())) for _ in range(int(input()))),
    key=itemgetter(1)):
    if t[0] >= s:
        s = t[1]
        c += 1
print(c)