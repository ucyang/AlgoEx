import sys

input = lambda: sys.stdin.readline().rstrip()

a, b = 0, 1
for i in range(int(input())):
    a, b = b, (a + b) % 10007
print(b)