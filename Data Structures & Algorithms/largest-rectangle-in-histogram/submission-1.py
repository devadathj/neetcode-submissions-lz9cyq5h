from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        output = 0
        check = deque()

        for i in range(len(heights)):
            
            index = i
            while check and heights[i] <= check[-1][1]:
                output = max(output, (i - check[-1][0]) * check[-1][1])
                index = check[-1][0]
                check.pop()
            
            check.append((index, heights[i]))

        for i in range(len(check)):
            output = max((len(heights) - check[i][0]) * check[i][1], output)

        return output