class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_product = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_product[i] = nums[i - 1] * prefix_product[i - 1]

        suffix_product = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix_product[i] = nums[i + 1] * suffix_product[i + 1]

        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix_product[i] * suffix_product[i]

        return output

