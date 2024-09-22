import sys

input = lambda: sys.stdin.readline().rstrip()

A, B, C = map(int, input().split())

A %= C
result = 1

while B:
    if B % 2:
        result = result * A % C
        B -= 1
    else:
        A = A * A % C
        B /= 2

print(result)
