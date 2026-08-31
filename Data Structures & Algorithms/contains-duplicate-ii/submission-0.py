class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        checker = set()

        l = 0

        for r in range(len(nums)):
            if r - l > k:
                checker.remove(nums[l])
                l += 1
            if nums[r] in checker:
                return True
            
            checker.add(nums[r])

        return False
