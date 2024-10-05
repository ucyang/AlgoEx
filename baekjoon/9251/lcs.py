import sys

input = lambda: sys.stdin.readline().rstrip()

A = input()
B = input()

if len(A) > len(B):
    A, B = B, A

dp = [0] * (len(A) + 1)

for b in B:
    t = dp[0]

    for i, a in enumerate(A, start=1):
        if a == b:
            t, dp[i] = dp[i], t + 1
        else:
            t, dp[i] = dp[i], max(dp[i], dp[i - 1])

print(dp[-1])
