l = int(input())
s = input()

result = 0
for i in range(l):
    result = (result + (ord(s[i]) - ord("a") + 1) * 31 ** i) % 1234567891

print(result)
