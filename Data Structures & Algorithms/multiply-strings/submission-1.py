class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == "0" or num2 == "0":
            return "0"

        output_num = int(num1) * int(num2)
        output = []
    
        while output_num:
            output.append(str(output_num % 10))
            output_num //= 10

        return "".join(reversed(output))
