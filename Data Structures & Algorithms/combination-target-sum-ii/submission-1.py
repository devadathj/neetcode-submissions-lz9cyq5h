class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        self.output = []

        def check_sum(i, arr):

            if sum(arr) == target:
                self.output.append(arr.copy())
                return

            if sum(arr) > target or i >= len(candidates):
                return

            arr.append(candidates[i])
            check_sum(i + 1, arr)
            arr.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
                
            check_sum(i + 1, arr)

        check_sum(0, [])

        return self.output
