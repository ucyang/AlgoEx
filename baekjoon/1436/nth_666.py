import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
i = 666
c = 0
while True:
    if str(i).find("666") != -1:
        c += 1
        if c == n:
            print(i)
            break
    i += 1
