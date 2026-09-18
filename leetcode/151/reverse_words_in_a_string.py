class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = s.split()
        splitted.reverse()

        return " ".join(splitted)
