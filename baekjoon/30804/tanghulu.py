import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = list(map(int, input().split()))

fruits = {S[0]: 1}
front, back = 0, 0
max_count = 1

while True:
    if len(fruits) < 3:
        back += 1

        if back >= N:
            if back - front > max_count:
                max_count = back - front
            break

        if S[back] in fruits:
            fruits[S[back]] += 1
        else:
            fruits[S[back]] = 1
    else:
        if fruits[S[front]] > 1:
            fruits[S[front]] -= 1
        else:
            del fruits[S[front]]

        front += 1

    if back - front > max_count:
        max_count = back - front

print(max_count)
