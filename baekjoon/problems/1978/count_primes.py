import sys

input = lambda: sys.stdin.readline().rstrip()


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2

    sqrt_n = n ** 0.5
    while i <= sqrt_n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True


input()
print(sum(map(lambda x: is_prime(int(x)), input().split())))
