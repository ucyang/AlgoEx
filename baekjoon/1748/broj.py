N = int(input())

n = N // 10
d = len(str(N))

a = 1
b = 9

s = 0

while n:
    s += a * b
    n //= 10
    a += 1
    b *= 10

s += (N - 10 ** (d - 1) + 1) * d

print(s)
