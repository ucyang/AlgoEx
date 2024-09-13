import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
order_counts = map(int, input().split())
T, P = map(int, input().split())

print(sum([count // T + bool(count % T) for count in order_counts]))
print(N // P, N % P)
