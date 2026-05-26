class Solution:
    def rob(self, nums: List[int]) -> int:
        
        num_houses = len(nums)
        cum_val = {}

        def rob_next(i):
            if i >= num_houses:
                return 0
            
            if i in cum_val:
                return cum_val[i]
            
            cum_val[i] = nums[i] + max(rob_next(i + 2), rob_next(i + 3))
            return cum_val[i]
            
        return max(rob_next(0), rob_next(1))