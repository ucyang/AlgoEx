import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
T = []
P = []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)


def get_max_p(n_start: int) -> int:
    max_p = 0

    for n in range(n_start, N):
        if n + T[n] <= N:
            p = P[n] + get_max_p(n + T[n])
            if p > max_p:
                max_p = p

    return max_p


print(get_max_p(0))
