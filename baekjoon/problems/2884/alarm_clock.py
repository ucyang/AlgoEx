h, m = map(int, input().split())

m -= 45
if m < 0:
    h = h - 1 if h > 0 else 23
    m += 60

print(h, m)
