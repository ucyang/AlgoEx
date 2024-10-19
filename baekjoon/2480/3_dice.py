from collections import Counter

c = Counter(map(int, input().split())).most_common()

if c[0][1] == 3:
    print(10000 + c[0][0] * 1000)
elif c[0][1] == 2:
    print(1000 + c[0][0] * 100)
else:
    print(sorted(c)[-1][0] * 100)
