class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()

        def calculate_distance(row, col, dist):
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return

            if grid[row][col] != 2147483647:
                return

            grid[row][col] = dist
            q.append((row, col))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))

        dist = 1
        while q:
            for i in range(len(q)):
                curr = q.popleft()

                for direction in directions:
                    calculate_distance(curr[0] + direction[0], curr[1] + direction[1], dist)

            dist += 1
