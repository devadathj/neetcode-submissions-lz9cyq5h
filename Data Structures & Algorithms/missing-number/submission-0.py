class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        high = len(nums)
        xorr = high

        for i in range(high):
            xorr ^= i ^ nums[i]

        return xorr