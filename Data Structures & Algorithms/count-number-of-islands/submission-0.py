class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        output = 0

        def check_land(row, col):

            if not 0 <= row < ROWS or not 0 <= col < COLS:
                return 

            if grid[row][col] != "1":
                return 

            grid[row][col] = "0"

            check_land(row + 1, col)
            check_land(row - 1, col)
            check_land(row, col + 1)
            check_land(row, col - 1)

            return

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    output += 1 
                    check_land(i, j)

        return output
