import sys

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())

    i = x
    while i <= M * N:
        if (i - y) % N == 0:
            print(i)
            break
        i += M
    else:
        print(-1)