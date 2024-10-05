class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ret = [nums[0]]
        for i in range(1, len(nums)):
            ret.append(ret[-1] + nums[i])
        return ret
