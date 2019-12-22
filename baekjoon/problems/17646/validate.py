#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    data = f.readlines()

success_count = 0
i = 0
while i < len(data):
    try:
        n = int(data[i])
        factors = data[i + 2].split()

        if len(factors) != int(data[i + 1]):
            print("%d = The number of factors is incorrect!" % n)
        elif any(not f.isdigit() for f in factors):
            print("%d = Some factors are not positive integers!" % n)
        elif sum(map(lambda x: int(x) ** 2, factors)) != n:
            print("%d = The sum of factors is incorrect!" % n)
        else:
            print("%d = " % n + " + ".join(factors))
            success_count += 1
    except:
        break

    i += 9

print("Succeeded: %d, Failed: %d"
      % (success_count, len(data) / 9 - success_count))
