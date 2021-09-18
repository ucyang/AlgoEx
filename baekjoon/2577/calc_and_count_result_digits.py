from collections import Counter

a, b, c = int(input()), int(input()), int(input())
n = Counter(str(a * b * c))

for i in range(10):
    print(n[str(i)])
