class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        repeat_check = set()

        for num in nums:
            if num in repeat_check:
                return True
            
            repeat_check.add(num)

        return False