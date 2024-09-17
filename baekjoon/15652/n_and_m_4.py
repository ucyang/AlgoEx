import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())


def dfs(start_n, m, last_seq):
    for n in range(start_n, N + 1):
        if m > 1:
            dfs(n, m - 1, last_seq + [n])
        else:
            print(*(last_seq + [n]))


dfs(1, M, [])
