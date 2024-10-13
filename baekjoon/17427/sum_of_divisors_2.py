N = int(input())
g = 0

for i in range(1, N + 1):
    g += N // i * i

print(g)
