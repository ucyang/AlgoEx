#!/usr/bin/env python3
# Make random parameters.

import sys
import random

# Check parameters.
if len(sys.argv) < 6:
    print("Please specify arguments correctly.")
    print("Usage: mkrandparam.py count x_min x_max y_min y_max [z_min z_max]")
    sys.exit(0x1)

dim = 3 if len(sys.argv) == 8 else 2

count = int(sys.argv[1])

x_min = float(sys.argv[2])
x_max = float(sys.argv[3])

y_min = float(sys.argv[4])
y_max = float(sys.argv[5])

if dim == 3:
    z_min = float(sys.argv[6])
    z_max = float(sys.argv[7])

print(count)

for i in range(count):
    if dim == 2:
        print(int(round(random.uniform(x_min, x_max))),
              int(round(random.uniform(y_min, y_max))))
    else:
        print(int(round(random.uniform(x_min, x_max))),
              int(round(random.uniform(y_min, y_max))),
              int(round(random.uniform(z_min, z_max))))
