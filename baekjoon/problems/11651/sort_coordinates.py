for p in sorted([tuple(map(int, input().split()[::-1])) for _ in range(int(input()))]):
    print(*p[::-1])
