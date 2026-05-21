class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        result = 0
        carry = 0
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            result |= (a_bit ^ b_bit ^ carry) << i

            carry =  a_bit + b_bit + carry > 1

        if result > 0x7FFFFFFF:
            result = ~(result ^ 0xFFFFFFFF)
            
        return result