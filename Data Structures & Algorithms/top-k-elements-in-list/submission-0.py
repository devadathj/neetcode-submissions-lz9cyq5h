class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        element_count = {}
        for num in nums:
            element_count[num] = element_count.get(num, 0) + 1

        frequency_count = [[] for i in range(len(nums) + 1)]
        for num, count in element_count.items():
             frequency_count[count].append(num)

        output = []
        for i in range(len(frequency_count) - 1, 0, -1):
            output.extend(frequency_count[i])

            if len(output) >= k:
                return output

