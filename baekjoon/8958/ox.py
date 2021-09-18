#!/usr/bin/env python3

for i in range(int(input())):
    s = input().split("X")
    p = 0
    for t in s:
        n = len(t)
        p += n * (n + 1) / 2
    print(int(p))
