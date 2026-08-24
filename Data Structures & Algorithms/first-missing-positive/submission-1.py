class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        i = 0

        while i < n:
            if 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
                