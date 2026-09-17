import sys

input = lambda: sys.stdin.readline().rstrip()


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        threshold = max(candies) - extraCandies
        return [True if c >= threshold else False for c in candies]
