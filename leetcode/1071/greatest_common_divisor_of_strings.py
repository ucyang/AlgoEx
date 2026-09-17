class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            s1, s2 = str1, str2
        else:
            s1, s2 = str2, str1

        n1, n2 = len(s1), len(s2)
        n_gcd = gcd(n1, n2)

        for i in range(1, n1 + 1):
            if n_gcd % i == 0:
                n_d = n_gcd // i
                for j in range(n_d, n1, n_d):
                    if s1[:n_d] != s1[j:j + n_d]:
                        break
                else:
                    if n2 % n_d == 0:
                        for j in range(0, n2, n_d):
                            if s1[:n_d] != s2[j:j + n_d]:
                                break
                        else:
                            return s1[:n_d]

        return ""
