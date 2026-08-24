class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        checker = 0

        for num in nums:
            if num > 0:
                checker |= 1<<(num - 1)

        counter = 1
        while checker:
            bit = checker & 1
            if not bit:
                return counter
            checker >>= 1
            counter += 1

        return counter