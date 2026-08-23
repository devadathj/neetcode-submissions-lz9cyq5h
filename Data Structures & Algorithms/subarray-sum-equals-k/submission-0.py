class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = {0 : 1}

        total = 0
        output = 0
        for num in nums:
            total += num
            diff = total - k
            if diff in prefix:
                output += prefix[diff]

            prefix[total] = 1 + prefix.get(total, 0)

        return output