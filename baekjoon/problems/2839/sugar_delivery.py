n = int(input())
i = n // 5

while i >= 0:
    q, r = divmod(n - 5 * i, 3)
    if r == 0:
        print(i + q)
        break
    i -= 1

if i < 0:
    print(-1)
