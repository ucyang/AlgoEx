import sys

input = lambda: sys.stdin.readline().rstrip()

s = []
for _ in range(int(input())):
    t = input().split()
    if t[0] == "push_front":
        s.insert(0, t[1])
    elif t[0] == "push_back":
        s.append(t[1])
    elif t[0] == "pop_front":
        if len(s):
            print(s[0])
            s.pop(0)
        else:
            print(-1)
    elif t[0] == "pop_back":
        if len(s):
            print(s[-1])
            s.pop()
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
