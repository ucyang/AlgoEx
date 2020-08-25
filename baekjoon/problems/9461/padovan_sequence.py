import sys

input = lambda: sys.stdin.readline().rstrip()

l = [1, 1, 1, 2, 2]
for _ in range(100 - len(l)):
    l.append(l[-1] + l[-5])
for _ in range(int(input())):
    print(l[int(input()) - 1])