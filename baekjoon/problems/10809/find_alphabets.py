import string

s = input()
for c in string.ascii_lowercase:
    if c != "a":
        print(" ", end="")
    print(s.find(c), end="")
