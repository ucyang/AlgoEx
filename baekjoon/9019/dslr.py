import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    queue = deque([(A, "")])
    seen = {A}

    while queue:
        num, commands = queue.popleft()

        if num == B:
            print(commands)
            break

        d = "%04d" % num

        candidates = {
            "D": 2 * num % 10000,
            "S": num - 1 if num > 0 else 9999,
            "L": int(d[1:] + d[0]),
            "R": int(d[-1] + d[:-1]),
        }

        for c, n in candidates.items():
            if n not in seen:
                queue.append((n, commands + c))
                seen.add(n)
