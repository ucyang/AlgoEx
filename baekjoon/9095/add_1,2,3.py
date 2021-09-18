import sys

input = lambda: sys.stdin.readline().rstrip()

d = [0] * 11

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, len(d)):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

for _ in range(int(input())):
    print(d[int(input())])