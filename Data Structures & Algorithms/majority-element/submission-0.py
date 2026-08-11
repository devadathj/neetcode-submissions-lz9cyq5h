class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        output = 0
        count = 0

        for num in nums:
            if count == 0:
                output = num

            if num == output:
                count += 1
            else:
                count -= 1

        return output