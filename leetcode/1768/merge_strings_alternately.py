class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        for i in range(len(word1) + len(word2)):
            try:
                merged.append(word1[i])
            except:
                pass
            try:
                merged.append(word2[i])
            except:
                pass

        return "".join(merged)
