class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        len_flowerbed = len(flowerbed)
        count = 0

        i = 0
        while i < len_flowerbed:
            if flowerbed[i] == 0:
                if i > 0 and flowerbed[i - 1] == 1:
                    i += 1
                    continue
                if i < len_flowerbed - 1 and flowerbed[i + 1] == 1:
                    i += 3
                    continue

                flowerbed[i] = 1
                count += 1

            i += 2

        return count >= n
