import sys
import re

input = lambda: sys.stdin.readline().rstrip()

s = 0
add = True
for x in re.split(r"(\D)", input()):
    if x.isnumeric():
        x = int(x)
        if add:
            s += x
        else:
            s -= x
    elif x == "-":
        add = False
print(s)