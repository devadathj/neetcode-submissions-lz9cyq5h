class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        output = nums[0]
        current_total = nums[0]

        for i in range(1, len(nums)):
            current_total = max(nums[i] + current_total, nums[i])
            output = max(output, current_total)

        return output



                