m = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        last_biggest = 0

        for c in reversed(s):
            n = m[c]
            if n < last_biggest:
                result -= n
            else:
                result += n
                last_biggest = n

        return result
