import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def bin_search(low, high):
            if low > high:
                return low
            
            mid = (low + high) // 2

            temp_time = 0
            for i in piles:
                temp_time += math.ceil(i / mid)
            
            if temp_time > h:
                return bin_search(mid + 1, high)
            elif temp_time <= h:
                return bin_search(low, mid - 1)

        return bin_search(1, max(piles))
