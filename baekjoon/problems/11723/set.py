import sys

input = lambda: sys.stdin.readline().rstrip()

s = set()
for _ in range(int(input())):
    t = input().split()
    if t[0] == "all":
        s.update(range(1, 21))
    elif t[0] == "empty":
        s.clear()
    else:
        x = int(t[1])
        if t[0] == "add":
            s.add(x)
        elif t[0] == "remove":
            s.discard(x)
        elif t[0] == "check":
            print(1 if x in s else 0)
        elif t[0] == "toggle":
            if x in s:
                s.remove(x)
            else:
                s.add(x)