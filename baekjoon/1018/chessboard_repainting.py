import sys

input = lambda: sys.stdin.readline().rstrip()

cases = (("WBWBWBWB",
          "BWBWBWBW",
          "WBWBWBWB",
          "BWBWBWBW",
          "WBWBWBWB",
          "BWBWBWBW",
          "WBWBWBWB",
          "BWBWBWBW"),

         ("BWBWBWBW",
          "WBWBWBWB",
          "BWBWBWBW",
          "WBWBWBWB",
          "BWBWBWBW",
          "WBWBWBWB",
          "BWBWBWBW",
          "WBWBWBWB"))

n, m = map(int, input().split())
b = [input() for _ in range(n)]

min_count = -1
for i in range(n - 7):
    for j in range(m - 7):
        for case in cases:
            count = 0
            for k in range(8):
                count += sum(b[i + k][j + t] != case[k][t] for t in range(8))
            if count < min_count or min_count == -1:
                min_count = count
print(min_count)
