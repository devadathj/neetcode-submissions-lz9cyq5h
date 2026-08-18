class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def possible(max_weight):
            ships = 1
            total = 0

            for w in weights:
                if total + w <= max_weight:
                    total += w
                else:
                    ships += 1
                    total = w

                    if ships > days:
                        return False

            return True


        low = max(weights)
        high = sum(weights)

        output = float("inf")
        while low <= high:
            mid = (low + high) // 2

            if possible(mid):
                output = min(output, mid)
                high = mid - 1
            else:
                low = mid + 1

        return output
