from collections import Counter

s = input().upper()
if len(s) <= 1:
    print(s)
else:
    l = Counter(s).most_common(2)
    print(l[0][0] if l[0][1] != l[1][1] else "?")
