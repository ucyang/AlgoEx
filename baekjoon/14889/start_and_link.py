import sys
from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

TEAM = set(range(N))


def get_score(team: set) -> int:
    score = 0

    for i, j in permutations(team, 2):
        score += S[i][j]

    return score


def get_min_diff_score(n: int, idx: int = 0, team: set = set()) -> int:
    min_diff_score = int(1e9)

    for i in range(idx, N - n + 1):
        t = team | {i}

        if n > 1:
            diff_score = get_min_diff_score(n - 1, i + 1, t)
        else:
            diff_score = abs(get_score(t) - get_score(TEAM - t))

        if diff_score < min_diff_score:
            min_diff_score = diff_score

    return min_diff_score


print(get_min_diff_score(N // 2))
