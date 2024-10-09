E, S, M = map(int, input().split())

year = S - 1
while True:
    if (year % 15 == E - 1
        and year % 19 == M - 1):
        break

    year += 28

print(year + 1)
