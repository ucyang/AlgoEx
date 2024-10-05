class Solution:
    def numberOfSteps(self, num: int) -> int:
        c = 0
        for i in format(num, "b"):
            if i == "0":
                c += 1
            else:
                c += 2
        return c - 1
