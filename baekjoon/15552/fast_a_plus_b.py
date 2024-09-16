import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    print(sum(map(int, input().split())))
