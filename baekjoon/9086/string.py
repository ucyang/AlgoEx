import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    s = input()
    print(s[0] + s[-1])
