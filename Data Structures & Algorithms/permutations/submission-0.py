class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []

        def generate_permutations(arr, check):
            if len(arr) == len(nums):
                output.append(arr.copy())
                return

            for i in range(len(nums)):
                if not check[i]:
                    arr.append(nums[i])
                    check[i] = True
                    generate_permutations(arr, check)
                    check[i] = False
                    arr.pop()
            
        generate_permutations([], [False] * len(nums))

        return output