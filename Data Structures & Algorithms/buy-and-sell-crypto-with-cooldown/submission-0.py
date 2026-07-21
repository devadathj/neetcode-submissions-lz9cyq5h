class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best_price = {}

        def cal_profit(i, state):
            if i >= len(prices):
                return 0

            if (i, state) in best_price:
                return best_price[(i, state)]

            if state:
                next_move = cal_profit(i + 1, False) - prices[i]
            else:
                next_move = cal_profit(i + 2, True) + prices[i]

            cooldown = cal_profit(i + 1, state)
            best_price[(i, state)] = max(next_move, cooldown)

            return best_price[(i, state)]

        return cal_profit(0, True)
