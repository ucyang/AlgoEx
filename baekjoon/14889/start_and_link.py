import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

TEAM = set(range(N))


def get_score(team: set) -> int:
    score = 0

    for i, j in combinations(team, 2):
        score += S[i][j] + S[j][i]

    return score


min_diff_score = int(1e9)

for team in combinations(range(N), N // 2):
    t = set(team)
    diff_score = abs(get_score(t) - get_score(TEAM - t))

    if diff_score < min_diff_score:
        min_diff_score = diff_score

print(min_diff_score)
