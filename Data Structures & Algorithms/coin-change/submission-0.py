class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        min_den_map = [float("inf")] * (amount + 1)
        min_den_map[0] = 0

        for i in range(1, amount + 1):
            for j in coins:
                if i - j >= 0:
                    min_den_map[i] = min(min_den_map[i], 1 + min_den_map[i - j])

        return min_den_map[amount] if min_den_map[amount] != float("inf") else -1