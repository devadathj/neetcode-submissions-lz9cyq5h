class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost_counter = {}

        def cal_cost(step):

            if step >= len(cost):
                return 0

            step1 = step + 1
            if step1 not in cost_counter:
                cost_counter[step1] = cal_cost(step1)

            step2 = step + 2
            if step2 not in cost_counter:
                cost_counter[step2] = cal_cost(step2)

            return cost[step] + min(cost_counter[step1], cost_counter[step2])

        return min(cal_cost(0), cal_cost(1))