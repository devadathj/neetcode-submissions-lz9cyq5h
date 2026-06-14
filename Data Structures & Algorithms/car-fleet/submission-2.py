import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        result = []

        combined = sorted(zip(position, speed), reverse=True)

        result.append((target - combined[0][0]) / combined[0][1])

        for i in range(1, len(position)):
            time = (target - combined[i][0]) / combined[i][1]
            if time > result[-1]:
                result.append(time)

        return len(result)