import sys

input = lambda: sys.stdin.readline().rstrip()

primes_test = [True] * 1000000
primes = []

for i in range(3, 1000000, 2):
    if primes_test[i]:
        primes.append(i)
        for j in range(2 * i, 1000000, i):
            primes_test[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    for p in primes:
        if primes_test[n - p]:
            print(n, "=", p, "+", n - p)
            break
