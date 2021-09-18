import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

h = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(h, (abs(x), x))
    else:
        print(heapq.heappop(h)[1] if len(h) else 0)