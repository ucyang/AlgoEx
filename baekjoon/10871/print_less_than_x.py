_, x = map(int, input().split())
flag = False
for a in map(int, input().split()):
    if a < x:
        print(" " + str(a) if flag else a, end="")
        flag = True
