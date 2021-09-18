import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

l = {n}
count = 0
while True:
    if 1 in l:
        break
    l2 = set()
    for i in l:
        if i % 3 == 0:
            l2.add(i / 3)
        if i % 2 == 0:
            l2.add(i / 2)
        l2.add(i - 1)
    l = l2
    count += 1

print(count)