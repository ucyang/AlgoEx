import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

for t in range(int(input())):
    p = input()
    n = int(input())
    a = input()
    d = deque(map(int, a[1:-1].split(",")) if n else ())
    
    if p.count("D") > len(d):
        print("error")
        continue
    p.replace("RR", "")

    rev = False
    for f in p:
        if f == "R":
            rev = not rev
        else:
            if rev:
                d.pop()
            else:
                d.popleft()

    print(str(list(reversed(d) if rev else d)).replace(" ", ""))