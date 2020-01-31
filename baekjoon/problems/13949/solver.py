#!/usr/bin/env python3
# Reference: https://mysteryzone.tistory.com/8

k, n = map(int, input().split())
used_tuples = set((0, 0, 1))
used_values = set([0])
queue = [(0, 0, 1)]
count = 1

for (a, b, c) in queue:
    for _ in range(3):
        t = k * (b + c) - a
        if t > 0:
            tt = tuple(sorted([t, b, c]))
            if tt not in used_tuples:
                used_tuples.add(tt)
                queue.append(tt)
        a, b, c = b, c, a
    if a not in used_values and b not in used_values and c not in used_values \
            and a != b != c:
        used_values.add(a)
        used_values.add(b)
        used_values.add(c)
        print(a, b, c)
        if count == n:
            break
        count += 1
