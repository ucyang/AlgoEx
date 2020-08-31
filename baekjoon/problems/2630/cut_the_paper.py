import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
l = [input().split() for _ in range(n)]
w = 0
b = 0

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
        if v == "0":
            global w
            w += 1
        else:
            global b
            b += 1
    else:
        n //= 2
        f(x, y, n)
        f(x + n, y, n)
        f(x, y + n, n)
        f(x + n, y + n, n)

f(0, 0, n)
print(w)
print(b)