class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        tracker = {}

        def cal_path(row, col, pre_val):
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return 0

            if pre_val >= matrix[row][col]:
                return 0

            if (row, col) in tracker:
                return tracker[(row, col)]

            max_val = 0
            for direction in directions:
                max_val = max(max_val, cal_path(row + direction[0], col + direction[1], matrix[row][col]))

            tracker[(row, col)] = 1 + max_val

            return tracker[(row, col)]

        cal_path(0, 0, -1)

        max_val = 0
        for i in range(ROWS):
            for j in range(COLS):
                max_val = max(max_val, cal_path(i, j, -1))

        return max_val
