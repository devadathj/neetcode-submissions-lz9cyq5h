class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        output = 0

        def calculate_area(row, col):
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return 0

            if grid[row][col] != 1:
                return 0

            grid[row][col] = 0
            count = 1
            for direction in directions:
                count += calculate_area(row + direction[0], col + direction[1])

            return count

        for i in range(ROWS):
            for j in range(COLS):
                output = max(output, calculate_area(i, j))

        return output
        