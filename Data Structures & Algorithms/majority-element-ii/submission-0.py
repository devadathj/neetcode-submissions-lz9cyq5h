class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if len(count) > 2:

                new_count = defaultdict(int)
                for key, val in count.items():
                    if val > 1:
                        new_count[key] = val - 1

                count = new_count

        output = []

        for num in count:
            if nums.count(num) > len(nums) / 3:
                output.append(num)

        return output
