import sys

input = lambda: sys.stdin.readline().rstrip()

g = [1] * 1000001
g[0] = 0

for i in range(2, 1000001):
    for j in range(i, 1000001, i):
        g[j] += i
    g[i] += g[i - 1]

N = [int(input()) for _ in range(int(input()))]

for n in N:
    print(g[n])
