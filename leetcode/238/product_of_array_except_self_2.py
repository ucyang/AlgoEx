class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        zero_val_idx = -1
        product_all = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_val_idx != -1:
                    return result
                zero_val_idx = i
            else:
                product_all *= nums[i]

        if zero_val_idx != -1:
            result[zero_val_idx] = product_all
        else:
            for i in range(len(nums)):
                result[i] = product_all // nums[i]

        return result
