import sys

input = lambda: sys.stdin.readline().rstrip()

handed = {int(input()) for _ in range(28)}
not_handed = set(range(1, 31)) - handed

for i in sorted(not_handed):
    print(i)
