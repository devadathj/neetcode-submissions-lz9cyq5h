class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]

        tracker = {}

        def cal_coins(l, r):
            if l > r:
                return 0

            if (l, r) in tracker:
                return tracker[(l, r)]

            tracker[(l, r)] = 0

            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1] + cal_coins(l, i - 1) + cal_coins(i + 1, r)
                tracker[(l, r)] = max(tracker[(l, r)], coins)

            return tracker[(l, r)]

        return cal_coins(1, len(nums) - 2)