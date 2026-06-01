class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        lismap = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            current_extra = 0
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    current_extra = max(current_extra, lismap[j])

            lismap[i] += current_extra

        return max(lismap)