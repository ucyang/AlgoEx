from itertools import combinations

heights = [int(input()) for _ in range(9)]

for p in combinations(heights, 7):
    if sum(p) == 100:
        print(*sorted(p), sep="\n")
        break
