class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.output = []

        def level_sum(i, current_array):
            if sum(current_array) == target:
                self.output.append(current_array.copy())
                return

            if sum(current_array) > target:
                return

            for j in range(i, len(nums)):
                current_array.append(nums[j])
                level_sum(j, current_array)
                current_array.pop()
                
        level_sum(0, [])
        return self.output
        
            