import sys

input = lambda: sys.stdin.readline().rstrip()

for i in range(int(input())):
    print("Case #%d: %d" % (i + 1, sum(map(int, input().split()))))
