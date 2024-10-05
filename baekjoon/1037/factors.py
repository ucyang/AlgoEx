_ = input()

min_factor = 1e9
max_factor = 0

for factor in map(int, input().split()):
    if min_factor > factor:
        min_factor = factor
    if max_factor < factor:
        max_factor = factor

print(min_factor * max_factor)
