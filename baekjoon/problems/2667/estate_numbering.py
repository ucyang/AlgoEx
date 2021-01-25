import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = [list(map(int, input())) for _ in range(N)]

t = []
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            c = 0
            q = [(j, i)]
            while q:
                x, y = q.pop(0)
                if 0 <= x < N and 0 <= y < N and A[y][x] == 1:
                    c += 1
                    A[y][x] = -1
                    q += [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
            t.append(c)

t.sort()
print(len(t))
for c in t:
    print(c)