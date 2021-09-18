import sys

input = lambda: sys.stdin.readline().rstrip()

s = []
for _ in range(int(input())):
    t = input().split()
    if t[0] == "push":
        s.append(t[1])
    elif t[0] == "pop":
        if len(s):
            print(s[0])
            s.pop(0)
        else:
            print(-1)
    elif t[0] == "size":
        print(len(s))
    elif t[0] == "empty":
        print(0 if len(s) else 1)
    elif t[0] == "front":
        print(s[0] if len(s) else -1)
    elif t[0] == "back":
        print(s[-1] if len(s) else -1)
