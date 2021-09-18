import sys

input = lambda: sys.stdin.readline().rstrip()

l = [tuple(map(int, input().split())) for _ in range(int(input()))]
result = []
for i in range(len(l)):
    c = 1
    for j in range(len(l)):
        if i == j:
            continue
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            c += 1
    result.append(c)
print(*result)
