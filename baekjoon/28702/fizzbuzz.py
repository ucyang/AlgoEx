import sys

input = lambda: sys.stdin.readline().rstrip()

for i in range(3):
    s = input()
    if s.isdigit():
        idx, n = i, int(s)

next = n + (3 - idx)

if next % 3 == 0 and next % 5 == 0:
    print("FizzBuzz")
elif next % 3 == 0:
    print("Fizz")
elif next % 5 == 0:
    print("Buzz")
else:
    print(next)
