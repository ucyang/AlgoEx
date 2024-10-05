class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        t_set = set()

        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            else:
                if t[i] in t_set:
                    return False
                d[s[i]] = t[i]
                t_set.add(t[i])

        return True
