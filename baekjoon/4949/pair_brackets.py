import sys

input = lambda: sys.stdin.readline().rstrip()

while True:
    s = input()
    if s == ".":
        break

    l = []
    flag = False
    for c in s:
        if c == "(" or c == "[":
            l.append(c)
        elif (c == ")" and (len(l) == 0 or l.pop() != "(")) \
                or (c == "]" and (len(l) == 0 or l.pop() != "[")):
            flag = True
            break

    print("no" if flag or len(l) else "yes")
