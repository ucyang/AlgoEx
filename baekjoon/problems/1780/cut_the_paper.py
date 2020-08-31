import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
l = [input().split() for _ in range(n)]
c = [0, 0, 0]

def f(x, y, n):
    v = l[y][x]
    t = True
    for i in range(y, y + n):
        for j in range(x, x + n):
            if l[i][j] != v:
                t = False
                break
        if not t:
            break
    if t:
        c[int(v)] += 1
    else:
        n //= 3
        for i in range(3):
            for j in range(3):
                f(x + n * j, y + n * i, n)

f(0, 0, n)
print(c[-1], c[0], c[1], sep="\n")