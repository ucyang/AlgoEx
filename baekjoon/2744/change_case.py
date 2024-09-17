import sys

input = lambda: sys.stdin.readline().rstrip()

word = input()
print("".join([c.upper() if c.islower() else c.lower() for c in word]))
