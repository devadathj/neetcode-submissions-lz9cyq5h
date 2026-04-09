class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        output = 0

        buy = prices[0]
        sell = 0

        for i in range(1, len(prices)):
            
            if prices[i] < buy:
                buy = prices[i]
                sell = 0
            elif prices[i] >= sell:
                sell = prices[i]
                output = max(output, sell - buy)

        return output
