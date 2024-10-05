class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        last_max_len = max_len = 0

        while r < len(s):
            if s[r] not in seen:
                max_len += 1
                seen.add(s[r])
                r += 1
            else:
                if max_len > last_max_len:
                    last_max_len = max_len
                while l < r:
                    seen.remove(s[l])
                    max_len -= 1
                    if s[l] == s[r]:
                        l += 1
                        break
                    else:
                        l += 1

        return max(max_len, last_max_len)
