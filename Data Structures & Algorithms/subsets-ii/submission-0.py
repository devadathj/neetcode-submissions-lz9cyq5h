class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        output = []

        count = Counter(nums)

        for key, val in count.items():
            new_batch = []

            for i in range(1, val + 1):
                new_set = [key] * i
                new_batch.append(new_set)
                for k in output:
                    new_batch.append(k + new_set)

            output.extend(new_batch)

        output.append([])

        return output

