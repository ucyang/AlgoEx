input()
l = list(map(int, input().split()))
l = list(map(lambda x: x / max(l) * 100, l))
print(sum(l) / len(l))
