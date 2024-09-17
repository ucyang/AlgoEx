import sys

input = lambda: sys.stdin.readline().rstrip()

while True:
    s = input()
    if not s:
        break
    print(s)
