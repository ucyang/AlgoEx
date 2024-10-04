import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

if N >= K:
    print(N - K)
else:
    q = deque([(N, 0)])
    visited = {N}

    while q:
        n, c = q.popleft()

        if n == K:
            print(c)
            break

        if 3 * n < 2 * K and 2 * n not in visited:
            q.appendleft((2 * n, c))
            visited.add(2 * n)
        if n - 1 >= 0 and n - 1 not in visited:
            q.append((n - 1, c + 1))
            visited.add(n - 1)
        if n + 1 <= K and n + 1 not in visited:
            q.append((n + 1, c + 1))
            visited.add(n + 1)
