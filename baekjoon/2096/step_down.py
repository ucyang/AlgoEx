import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

min_points = [0] * 3
max_points = [0] * 3

for _ in range(N):
    p0, p1, p2 = map(int, input().split())

    min_points = [
        p0 + min(min_points[0:2]),
        p1 + min(min_points[0:3]),
        p2 + min(min_points[1:3]),
    ]

    max_points = [
        p0 + max(max_points[0:2]),
        p1 + max(max_points[0:3]),
        p2 + max(max_points[1:3]),
    ]

print(max(max_points), min(min_points))
