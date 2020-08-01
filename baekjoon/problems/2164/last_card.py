import sys

input = lambda: sys.stdin.readline().rstrip()

l = tuple(range(1, int(input()) + 1))
i = 1
while len(l) > 1:
    odd_flag = len(l) % 2
    l = l[i::2]
    if odd_flag:
        i = not i
print(l[0])
