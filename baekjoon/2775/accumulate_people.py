from itertools import accumulate

for _ in range(int(input())):
    k, n = int(input()), int(input())
    s = range(1, n + 1)
    for _ in range(k):
        s = accumulate(s)
    print(list(s)[-1])
