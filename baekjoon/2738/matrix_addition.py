import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

C = [[aa + bb for aa, bb in zip(a, b)] for a, b in zip(A, B)]

for c in C:
    print(*c)
