class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = [[]]

        for i in nums:
            next_batch = []
            for j in output:
                next_batch.append(j + [i])

            output.extend(next_batch)
            
        return output