import sys

input = lambda: sys.stdin.readline().rstrip()

l = [int(input()) for _ in range(int(input()))]
num_stack = []
action_stack = []
last = 0
for v in l:
    if len(num_stack) and num_stack[-1] == v:
        num_stack.pop()
        action_stack.append("-")
    elif v > last:
        num_stack += range(last + 1, v)
        action_stack += ["+"] * (v - last) + ["-"]
        last = v
    else:
        action_stack = []
        break

if len(action_stack):
    print(*action_stack, sep="\n")
else:
    print("NO")