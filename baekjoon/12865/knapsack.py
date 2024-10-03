import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
items = []

for _ in range(N):
    W, V = map(int, input().split())
    if W <= K and V > 0:
        items.append((W, V))

dp =[[0] * (K + 1) for _ in range(len(items) + 1)]

for i, (w, v) in enumerate(items, start=1):
    for k in range(1, K + 1):
        if w > k:
            dp[i][k] = dp[i - 1][k]
        else:
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - w] + v)

print(dp[-1][-1])
