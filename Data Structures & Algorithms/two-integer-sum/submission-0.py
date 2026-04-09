class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index_hashmap = dict()

        for index, num in enumerate(nums):

            if target - num in index_hashmap:
                return sorted([index, index_hashmap[target - num]])

            if num not in index_hashmap.keys():
                index_hashmap[num] = index
            