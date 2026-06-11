class Solution:
    def trap(self, height: List[int]) -> int:
    
        output = 0

        left = 0
        right = len(height) - 1

        maxl = height[left]
        maxr = height[right]

        while left < right:
            if maxl <= maxr:
                left += 1
                if height[left] < min(maxl, maxr):
                    output += min(maxl, maxr) - height[left]
                maxl = max(maxl, height[left])
            else:
                right -= 1
                if height[right] < min(maxl, maxr):
                    output += min(maxl, maxr) - height[right]
                maxr = max(maxr, height[right])
        
        return output
