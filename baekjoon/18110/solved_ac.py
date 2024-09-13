import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
ratings = [int(input()) for _ in range(n)]

if n > 0:
    ratings.sort()

    k = n * 0.15
    if k - int(k) >= 0.5:
        k = int(k) + 1
    else:
        k = int(k)

    ratings = ratings[k:-k] if k else ratings

    average_rating = sum(ratings) / len(ratings)
    if average_rating - int(average_rating) >= 0.5:
        print(int(average_rating) + 1)
    else:
        print(int(average_rating))
else:
    print(0)
