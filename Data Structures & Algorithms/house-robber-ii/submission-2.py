class Solution:
    def rob(self, nums: List[int]) -> int:
        
        num_houses = len(nums)

        if num_houses == 1:
            return nums[0]

        cum_max = {}

        def tot_rob(i, flag):

            if i >= num_houses or (flag and i == num_houses - 1):
                return 0

            if (i, flag) in cum_max:
                return cum_max[(i, flag)]

            cum_max[(i, flag)] = max(nums[i] + tot_rob(i + 2, flag), tot_rob(i + 1, flag))
            return cum_max[(i, flag)]

        return max(tot_rob(0, True), tot_rob(1, False))

            