class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        tracker = {}

        def cal_target(index, value):
            if index == len(nums):
                return 1 if value == target else 0

            if (index, value) in tracker:
                return tracker[(index, value)]

            tracker[(index, value)] = cal_target(index + 1, value + nums[index]) + cal_target(index + 1, value - nums[index])

            return tracker[(index, value)]

        return cal_target(0, 0)