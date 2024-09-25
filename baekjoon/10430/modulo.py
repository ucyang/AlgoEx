import sys

input = lambda: sys.stdin.readline().rstrip()

A, B, C = map(int, input().split())

i = ((A % C) + (B % C)) % C
j = ((A % C) * (B % C)) % C

print(i)
print(i)
print(j)
print(j)
