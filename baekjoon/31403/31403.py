import sys

input = lambda: sys.stdin.readline().rstrip()

A, B, C = input(), input(), input()

print(int(A) + int(B) - int(C))
print(int(A + B) - int(C))
