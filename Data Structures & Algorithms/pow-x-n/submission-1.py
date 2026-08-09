class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            x = 1 / x
            n = -1 * n
            
        checker = {}

        def calc_power(num, exp):
            if exp in checker:
                return checker[exp]

            if exp == 1:
                return num

            if exp == 0:
                return 1

            checker[exp] = calc_power(num, exp // 2) * calc_power(num, exp - (exp // 2))

            return checker[exp]

        return calc_power(x, n)