import sys

input = lambda: sys.stdin.readline().rstrip()

for i in range(int(input())):
    A, B = map(int, input().split())
    print("Case #%d: %d + %d = %d" % (i + 1, A, B, A + B))
