class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        elif nums[0] < nums[-1]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        while nums[left] < nums[left + 1]:
            req_num = (left + right) // 2

            if nums[req_num] > nums[right]:
                left = req_num
            else:
                right = req_num

        return nums[left + 1] 