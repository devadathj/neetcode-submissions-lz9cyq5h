class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        output = 0

        for num in nums:

            if num - 1 not in nums:
                temp_output = 1
                temp_num = num
                while temp_num + 1 in nums:
                    temp_output += 1
                    temp_num += 1
                
                if temp_output > output:
                    output = temp_output
        
        return output