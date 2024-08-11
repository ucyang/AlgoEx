import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()


def minpop(d: dict, q: list) -> int:
    while True:
        i = heappop(q)
        if i in d:
            return i


def maxpop(d: dict, q: list) -> int:
    while True:
        i = -heappop(q)
        if i in d:
            return i


for _ in range(int(input())):
    d = {}
    minq, maxq = [], []
    count = {}

    for _ in range(int(input())):
        c, n = input().split()
        n = int(n)

        if c == "I":
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

            heappush(minq, n)
            heappush(maxq, -n)
        elif c == "D" and d:
            if n == 1:
                i = maxpop(d, maxq)
            elif n == -1:
                i = minpop(d, minq)

            if d[i] == 1:
                del d[i]
            else:
                d[i] -= 1

    if d:
        print(maxpop(d, maxq), minpop(d, minq))
    else:
        print("EMPTY")
