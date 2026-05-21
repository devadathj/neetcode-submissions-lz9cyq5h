class Solution:
    def countBits(self, n: int) -> List[int]:
        
        output = []
        output.append(0)
        power2 = 1

        for i in range(1, n + 1):
            if power2 * 2 == i:
                power2 = i
            output.append(1 + output[i - power2])

        return output