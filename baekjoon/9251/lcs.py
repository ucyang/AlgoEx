import sys

input = lambda: sys.stdin.readline().rstrip()

A = input()
B = input()

if len(A) > len(B):
    A, B = B, A

dp = [0] * (len(A) + 1)
dp_tmp = [0] * (len(A) + 1)

for b in B:
    for i, a in enumerate(A, start=1):
        if a == b:
            dp_tmp[i] = dp[i - 1] + 1
        else:
            dp_tmp[i] = max(dp[i], dp_tmp[i - 1])

    dp, dp_tmp = dp_tmp, dp

print(dp[-1])
