import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

c = 0
for a in reversed(A):
    c += K // a
    K %= a
print(c)