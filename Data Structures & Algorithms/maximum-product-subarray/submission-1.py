class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result = float('-inf')

        cur_min = 1
        cur_max = 1

        for i in nums:
            temp = cur_max * i
            cur_max = max(cur_max * i, cur_min * i, i)
            cur_min = min(temp, cur_min * i, i)
            result = max(result, cur_max)

        return result