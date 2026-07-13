class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        rotten_fruits = deque()
        time = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def update_fruits(row, col):
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return False
            
            if grid[row][col] != 1:
                return False
            
            grid[row][col] = 2
            rotten_fruits.append((row, col))

            return True

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    rotten_fruits.append((i, j))

        while rotten_fruits:
            switch = False
            for i in range(len(rotten_fruits)):
                curr = rotten_fruits.popleft()

                for direction in directions:
                    if update_fruits(curr[0] + direction[0], curr[1] + direction[1]):
                        switch = True

            if switch:
                time += 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1

        return time

