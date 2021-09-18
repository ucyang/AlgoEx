import sys
from decimal import Decimal, getcontext

input = lambda: sys.stdin.readline().rstrip()

def pi():
    getcontext().prec += 2
    three = Decimal(3)
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s

def sin(x):
    getcontext().prec += 2
    x %= 2 * PI
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i - 1)
        num *= x ** 2
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

def cos(x):
    getcontext().prec += 2
    x %= 2 * PI
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i - 1)
        num *= x ** 2
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

def f(x):
    return a * x + b * sin(x) + c

def f_prime(x):
    return a + b * cos(x)

def get_next_x(x):
    return x - f(x) / f_prime(x)

def newton_raphson():
    t = 0
    while True:
        x = get_next_x(t)
        if round(x, 8) == round(t, 8):
            break
        t = x
    return x

getcontext().prec = 100
PI = pi()
a, b, c = map(int, input().split())
print("{:.9f}".format(abs(newton_raphson())))