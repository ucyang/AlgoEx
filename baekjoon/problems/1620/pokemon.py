import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
l = [input() for _ in range(n)]
for _ in range(m):
    s = input()
    if s.isdigit():
        print(l[int(s) - 1])
    else:
        print(l.index(s) + 1)