import sys

input = lambda: sys.stdin.readline().rstrip()

H = int(input())
triangle = [list(map(int, input().split())) for _ in range(H)]

for i in range(1, H):
    triangle[i][0] += triangle[i - 1][0]
    triangle[i][-1] += triangle[i - 1][-1]

    for j in range(1, i):
        triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

print(max(triangle[-1]))
