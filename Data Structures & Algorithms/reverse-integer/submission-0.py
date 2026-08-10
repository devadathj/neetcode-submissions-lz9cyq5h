class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            neg_check = True
            x = -x
        else:
            neg_check = False

        output = 0

        while x:
            output = (output * 10) + (x % 10)
            x //= 10
        
        if neg_check:
            output = -output
            
        return output if -2 ** 31 <= output <= 2 ** 31 - 1 else 0