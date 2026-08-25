class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        checker = set()

        for num in nums:
            if num not in checker:
                checker.add(num)
            else:
                return True

        return False