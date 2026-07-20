class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        SIDE = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = {(0, 0)}
        minheap = [(grid[0][0], 0, 0)]

        while minheap:
            t, row, col = heapq.heappop(minheap)

            if (row, col) == (SIDE - 1, SIDE- 1):
                return t

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if (0 <= new_row < SIDE and 0 <= new_col < SIDE) and ((new_row, new_col) not in visited):
                    visited.add((new_row, new_col))
                    heapq.heappush(minheap, (max(t, grid[new_row][new_col]), new_row, new_col))
