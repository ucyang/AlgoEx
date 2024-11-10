N = int(input())

m = 1
s = 0

while N >= 10 * m:
    s += (9 * m) * len(str(m))
    m *= 10

s += (N - m + 1) * len(str(m))

print(s)
