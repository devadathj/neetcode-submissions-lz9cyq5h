class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n == 1:
            return True

        checker = set()

        while n not in checker:
            checker.add(n)
            next_num = 0

            while n: 
                next_num += (n % 10) ** 2
                n //= 10

            if next_num == 1:
                return True

            n = next_num
            
        return False
            