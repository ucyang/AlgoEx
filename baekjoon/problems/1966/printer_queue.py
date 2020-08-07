import sys

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    _, m = map(int, input().split())
    l = list(map(int, input().split()))
    i = 1
    while True:
        if l[0] == max(l):
            if m == 0:
                print(i)
                break
            l.pop(0)
            i += 1
        else:
            l.append(l.pop(0))
        
        m = m - 1 if m > 0 else len(l) - 1