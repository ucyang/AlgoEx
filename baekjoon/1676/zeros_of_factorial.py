import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

count_2 = 0
i = 2
while i <= n:
    count_2 += n // i
    i *= 2

count_5 = 0
i = 5
while i <= n:
    count_5 += n // i
    i *= 5

print(min(count_2, count_5))