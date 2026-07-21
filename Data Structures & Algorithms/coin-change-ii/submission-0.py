class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        tracker = {}

        def target_check(index, cur_target):
            if index >= len(coins):
                return 0
            
            if cur_target == 0:
                return 1

            if (index, cur_target) in tracker:
                return tracker[(index, cur_target)]

            output = 0
            if cur_target > 0:
                output = target_check(index + 1, cur_target) + target_check(index, cur_target - coins[index])

            tracker[(index, cur_target)] = output
            return output

        return target_check(0, amount)



       
