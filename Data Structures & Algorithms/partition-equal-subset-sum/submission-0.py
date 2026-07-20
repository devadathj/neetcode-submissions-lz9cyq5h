class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        req_sum = sum(nums)

        if req_sum % 2:
            return False

        req_sum = sum(nums) // 2

        check = {0}

        for num in nums:
            next_check = set()

            for i in check:
                next_check.add(i + num)

            if req_sum in next_check:
                return True

            check.update(next_check)

        return False