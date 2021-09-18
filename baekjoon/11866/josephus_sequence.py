n, k = map(int, input().split())

l = list(range(1, n + 1))
i = k - 1
size = len(l)
results = []
while True:
    results.append(l[i])
    l.pop(i)
    size -= 1
    if size == 0:
        break
    i = (i + k - 1) % size

print("<", end="")
print(*results, sep=", ", end="")
print(">")
