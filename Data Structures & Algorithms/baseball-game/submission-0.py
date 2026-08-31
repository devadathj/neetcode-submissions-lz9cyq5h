class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        output = []

        for operation in operations:
            if operation == "+":
                output.append(output[-1] + output[-2])
            elif operation == "C":
                output.pop()
            elif operation == "D":
                output.append(2 * output[-1])
            else:
                output.append(int(operation))

        return sum(output)