class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        i, j = -1, -1

        for k in range(1, len(nums)):
            if i != -1 and nums[j] < nums[k]:
                return True
            if nums[k - 1] < nums[k]:
                i, j = k - 1, k
            elif nums[i] < nums[k] < nums[j]:
                j = k

        return False
