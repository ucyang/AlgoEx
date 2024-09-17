import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))

accum_len = [0] * N

for i in range(N):
    accum_len_before = [accum_len[j] for j in range(i) if A[j] < A[i]]
    if accum_len_before:
        accum_len[i] = max(accum_len_before) + 1
    else:
        accum_len[i] = 1

print(max(accum_len))
