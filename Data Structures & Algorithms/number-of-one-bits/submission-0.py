class Solution:
    def hammingWeight(self, n: int) -> int:
        
        output = 0

        while n:
            n &= (n - 1)
            output += 1

        return output