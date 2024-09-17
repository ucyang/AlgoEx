import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
integers = list(map(int, input().split()))
v = int(input())

print(integers.count(v))
