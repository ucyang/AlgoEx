import sys

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    left_paren_count = 0
    for c in input():
        if c == "(":
            left_paren_count += 1
        elif c == ")":
            left_paren_count -= 1
            if left_paren_count < 0:
                break
    print("NO" if left_paren_count else "YES")
