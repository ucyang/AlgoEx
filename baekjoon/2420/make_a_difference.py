import sys

input = lambda: sys.stdin.readline().rstrip()

x, y = map(int, input().split())
print(abs(x - y))
