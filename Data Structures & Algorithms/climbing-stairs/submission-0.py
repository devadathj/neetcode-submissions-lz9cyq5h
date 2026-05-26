class Solution:
    def climbStairs(self, n: int) -> int:
        
        ways_per_step = {}

        def num_ways(n):
            
            if n == 0:
                return 1
            elif n < 0:
                return 0
            
            if n in ways_per_step:
                return ways_per_step[n]
            
            ways_per_step[n] = num_ways(n - 1) + num_ways(n - 2) 
            return ways_per_step[n]

        return num_ways(n)