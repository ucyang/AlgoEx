import sys

input = lambda: sys.stdin.readline().rstrip()

def f(l, x, y, w, h):
    n = l[y][x]
    flag = False
    for i in range(y, y + h):
        for j in range(x, x + w):
            if l[i][j] != n:
                flag = True
                break
        if flag:
            break
    
    if flag:
        w //= 2
        h //= 2
        return "(" + f(l, x, y, w, h) + f(l, x + w, y, w, h) \
             + f(l, x, y + h, w, h) + f(l, x + w, y + h, w, h) + ")"
    return n

N = int(input())
L = [list(input()) for _ in range(N)]
print(f(L, 0, 0, N, N))