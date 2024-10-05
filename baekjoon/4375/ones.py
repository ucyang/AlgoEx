import sys

input = lambda: sys.stdin.readline().rstrip()

while True:
    n = input()
    if not n:
        break

    n = int(n)
    i = 1
    while True:
        if i % n == 0:
            print(len(str(i)))
            break
        i = i * 10 + 1
