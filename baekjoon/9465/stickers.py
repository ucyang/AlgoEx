import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    if n > 1:
        stickers[0][1] += stickers[1][0]
        stickers[1][1] += stickers[0][0]

        for i in range(2, n):
            stickers[0][i] += max(stickers[0][i - 2], stickers[1][i - 2], stickers[1][i - 1])
            stickers[1][i] += max(stickers[1][i - 2], stickers[0][i - 2], stickers[0][i - 1])

    print(max(stickers[0][-1], stickers[1][-1]))
