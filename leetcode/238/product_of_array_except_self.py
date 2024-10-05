class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        try:
            zero_idx = nums.index(0)
            try:
                nums.index(0, zero_idx + 1)
                for i in range(len(nums)):
                    nums[i] = 0
            except:
                m = 1
                for i in range(len(nums)):
                    if i != zero_idx:
                        m *= nums[i]
                        nums[i] = 0
                nums[zero_idx] = m
        except:
            for i in range(1, len(nums)):
                nums[i] = nums[i - 1] * nums[i]
            if nums[-1]:
                product_all = nums[-1] if nums[-1] else nums[-2]
            else:
                product_all = nums[-2]
            for i in range(len(nums) - 1, 0, -1):
                nums[i] = product_all // nums[i] * nums[i - 1]
            nums[0] = product_all // nums[0]

        return nums
