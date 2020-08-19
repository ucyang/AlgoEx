import sys

input = lambda: sys.stdin.readline().rstrip()

l = [int(input()) for _ in range(int(input()))]
d = [0] * len(l)

try:
    d[0] = l[0]
    d[1] = l[0] + l[1]
    d[2] = max(l[0], l[1]) + l[2]

    for i in range(3, len(l)):
        d[i] = max(d[i - 2], d[i - 3] + l[i - 1]) + l[i]
except IndexError:
    pass

print(d[-1])