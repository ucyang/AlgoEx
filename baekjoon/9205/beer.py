import sys

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    a = [tuple(map(int, input().split())) for _ in range(int(input()) + 2)]
    q = [a.pop(0)]
    flag = False
    while q:
        x0, y0 = q.pop(0)
        i = 0
        while i < len(a):
            x, y = a[i]
            if abs(x - x0) + abs(y - y0) <= 1000:
                if i == len(a) - 1:
                    print("happy")
                    flag = True
                    break
                q.append(a.pop(i))
            else:
                i += 1
        if flag:
            break
    if not flag:
        print("sad")