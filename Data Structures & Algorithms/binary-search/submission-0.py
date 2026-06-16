class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bin_search(low, high, target):

            if low > high:
                return -1

            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return bin_search(low, mid - 1, target)
            else:
                return bin_search(mid + 1, high, target)

        return bin_search(0, len(nums) - 1, target) 