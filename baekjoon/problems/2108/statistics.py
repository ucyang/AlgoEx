import sys
from statistics import mean, median
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

l = [int(input()) for _ in range(int(input()))]
c = Counter(l).most_common()
most_common = [t[0] for t in c if t[1] == c[0][1]]
print(round(mean(l)))
print(median(l))
print(sorted(most_common)[1] if len(most_common) > 1 else most_common[0])
print(max(l) - min(l))
