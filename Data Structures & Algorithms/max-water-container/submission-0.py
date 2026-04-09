class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        output = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            volume = min(heights[left], heights[right]) * (right - left)

            if volume > output:
                output = volume

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return output