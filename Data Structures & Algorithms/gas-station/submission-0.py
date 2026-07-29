class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        output = 0
        net_gas = 0

        for i in range(len(gas)):
            net_gas += (gas[i] - cost[i])

            if net_gas < 0:
                net_gas = 0
                output = i + 1

        return output