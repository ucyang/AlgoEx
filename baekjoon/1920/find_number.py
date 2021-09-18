import sys

input = lambda: sys.stdin.readline().rstrip()

input()
s = set(map(int, input().split()))
input()
for i in map(int, input().split()):
    print(1 if i in s else 0)
