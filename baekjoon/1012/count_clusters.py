import sys

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    l = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        l[y][x] = 1
    c = 0
    for y in range(N):
        for x in range(M):
            if l[y][x] == 1:
                c += 1
                q = {(x, y)}
                while q:
                    p = q.pop()
                    i, j = p
                    l[j][i] = 2
                    for t in ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)):
                        i, j = t
                        if 0 <= i < M and 0 <= j < N and l[j][i] == 1:
                            q.add(t)
    print(c)