import sys

input = lambda: sys.stdin.readline().rstrip()

a = int(input())
b = int(input())

print(a * (b % 10))
print(a * (b // 10 % 10))
print(a * (b // 100 % 10))
print(a * b)
