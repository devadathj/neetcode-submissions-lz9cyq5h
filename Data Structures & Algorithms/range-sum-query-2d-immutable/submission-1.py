class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sum_mat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        for i in range(ROWS):
            for j in range(COLS):
                self.sum_mat[i + 1][j + 1] = matrix[i][j] + self.sum_mat[i][j + 1] + self.sum_mat[i + 1][j] - self.sum_mat[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_mat[row2 + 1][col2 + 1] - self.sum_mat[row2 + 1][col1] - self.sum_mat[row1][col2 + 1] + self.sum_mat[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)