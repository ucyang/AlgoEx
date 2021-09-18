import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
S = input()

x = 0
c = 0
for i in range(2, M):
    if S[i - 2] != S[i - 1] != S[i]:
        if S[i] == "I":
            c += 1
            if c >= N:
                x += 1
    else:
        c = 0
print(x)