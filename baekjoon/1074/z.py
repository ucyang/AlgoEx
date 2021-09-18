import sys

input = lambda: sys.stdin.readline().rstrip()

N, R, C = map(int, input().split())

count = 0
def f(i, j, n):
    if i == R and j == C:
        return True
    if not (i <= R < i + n and j <= C < j + n):
        global count
        count += n ** 2
        return False
    m = n // 2
    for r, c in ((i, j), (i, j + m), (i + m, j), (i + m, j + m)):
        if f(r, c, m):
            return True
    return False

f(0, 0, 2 ** N)
print(count)