import sys

input = lambda: sys.stdin.readline().rstrip()

input()
d = {}
for i in map(int, input().split()):
    d[i] = d[i] + 1 if i in d else 1
input()
print(*(d[i] if i in d else 0 for i in map(int, input().split())))
