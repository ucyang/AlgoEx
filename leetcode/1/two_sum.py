class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        i = 0
        j = len_nums - 1
        sorted_idx = sorted(range(len_nums), key=lambda k: nums[k])

        while i < j:
            s = nums[sorted_idx[i]] + nums[sorted_idx[j]]
            if s == target:
                break
            if s < target:
                i += 1
            else:
                j -= 1

        return [sorted_idx[i], sorted_idx[j]]
