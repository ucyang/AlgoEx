import sys

input = lambda: sys.stdin.readline().rstrip()

print(*sorted(int(input()) for _ in range(int(input()))), sep="\n")
