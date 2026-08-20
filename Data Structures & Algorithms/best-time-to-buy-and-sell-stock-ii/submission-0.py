class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        output = 0

        buy = float("inf")
        for i in prices:
            if i > buy:
                output += i - buy
            buy = i

        return output