import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()


def dfs(m, last_seq):
    for i in range(N):
        if num[i] in last_seq:
            continue
        if m > 1:
            dfs(m - 1, last_seq + [num[i]])
        else:
            print(*(last_seq + [num[i]]))


dfs(M, [])
