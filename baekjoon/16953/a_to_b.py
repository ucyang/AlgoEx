import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

A, B = map(int, input().split())

queue = deque([(A, 0)])

while queue:
    num, count = queue.popleft()

    if num == B:
        print(count + 1)
        break

    if num * 2 <= B:
        queue.append((num * 2, count + 1))
    if num * 10 + 1 <= B:
        queue.append((num * 10 + 1, count + 1))
else:
    print(-1)
