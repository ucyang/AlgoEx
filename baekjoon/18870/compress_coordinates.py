import sys
from operator import itemgetter

input = lambda: sys.stdin.readline().rstrip()

input()

l = []
for i, x in enumerate(input().split()):
    l.append([i, int(x)])
l.sort(key=itemgetter(1))

last_val = l[0][1]
last_count = 0
for i in range(len(l)):
    if l[i][1] != last_val:
        last_val = l[i][1]
        last_count += 1
    l[i][1] = last_count

l.sort()
for i in range(len(l)):
    if i:
        print(" ", end="")
    print(l[i][1], end="")
print()