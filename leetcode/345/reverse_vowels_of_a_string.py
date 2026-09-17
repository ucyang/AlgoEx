class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        l, h = 0, len(s) - 1

        while True:
            while l < h and s_list[l].lower() not in "aeiou":
                l += 1
            while l < h and s_list[h].lower() not in "aeiou":
                h -= 1

            if l >= h:
                break

            s_list[l], s_list[h] = s_list[h], s_list[l]

            l += 1
            h -= 1

        return "".join(s_list)
