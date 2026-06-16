import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = max(piles)

        output = high

        while low <= high:
        
            mid = (low + high) // 2

            temp_time = 0
            for i in piles:
                temp_time += math.ceil(i / mid)
            
            if temp_time > h:
                low = mid + 1
            else:
                output = mid
                high = mid - 1
               
        return output
