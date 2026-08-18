class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        output = set()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1
                req = target - nums[i] - nums[j]
                while left < right:
                    if nums[left] + nums[right] == req:
                        output.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] > req:
                        right -= 1
                    else:
                        left += 1

        return [list(x) for x in output]
