class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            s1, s2 = str1, str2
        else:
            s1, s2 = str2, str1

        n1, n2 = len(s1), len(s2)

        for d in range(1, n1 + 1):
            if n1 % d == 0:
                i = n1 // d
                for j in range(i, n1, i):
                    if s1[:i] != s1[j:j + i]:
                        break
                else:
                    if n2 % i == 0:
                        for j in range(0, n2, i):
                            if s1[:i] != s2[j:j + i]:
                                break
                        else:
                            return s1[:i]

        return ""
