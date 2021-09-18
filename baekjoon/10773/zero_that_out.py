import sys

input = lambda: sys.stdin.readline().rstrip()

l = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        l.pop()
    else:
        l.append(n)
print(sum(l))
