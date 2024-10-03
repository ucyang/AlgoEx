import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
items = []

for _ in range(N):
    W, V = map(int, input().split())
    if W <= K and V > 0:
        items.append((W, V))

dp =[0] * (K + 1)

for w, v in items:
    for k in range(K, w - 1, -1):
        dp[k] = max(dp[k], dp[k - w] + v)

print(dp[-1])
