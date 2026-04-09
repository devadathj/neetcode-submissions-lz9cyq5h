class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = set()

        for i in range(len(nums)):

            required_sum = -nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == required_sum:
                    output.add(tuple(sorted((nums[i], nums[left], nums[right]))))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < required_sum:
                    left += 1
                else:
                    right -= 1
            
        return [list(x) for x in output]