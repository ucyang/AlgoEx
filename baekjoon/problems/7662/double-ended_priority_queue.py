import sys
import bisect
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    q = deque()
    count = {}
    for _ in range(int(input())):
        c, n = input().split()
        n = int(n)
        if c == "I":
            if n in count:
                count[n] += 1
            else:
                bisect.insort(q, n)
                count[n] = 1
        elif c == "D" and q:
            if n == 1:
                if count[q[-1]] > 1:
                    count[q[-1]] -= 1
                else:
                    count.pop(q.pop())
            elif n == -1:
                if count[q[0]] > 1:
                    count[q[0]] -= 1
                else:
                    count.pop(q.popleft())
    if len(q):
        print(q[-1], q[0])
    else:
        print("EMPTY")