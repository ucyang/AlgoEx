class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        left_sum = [0, nums[0]]
        right_sum = [0, nums[-1]]

        for i in range(1, n - 1):
            left_sum.append(left_sum[-1] + nums[i])
            right_sum.append(right_sum[-1] + nums[n - i - 1])

        for i in range(n):
            if left_sum[i] == right_sum[n - i - 1]:
                return i

        return -1
