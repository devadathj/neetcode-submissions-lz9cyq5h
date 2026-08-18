class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = right = 0
        output = float("inf")

        total = 0
        while right < len(nums):
            total += nums[right]
            if total >= target:
                while left < right and total - nums[left] >= target:
                    total -= nums[left]
                    left += 1
                output = min(output, right - left + 1)
            right += 1

        return output if output != float("inf") else 0