class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS, COLS = len(matrix), len(matrix[0])

        top_row = False
        for i in range(COLS):
            if matrix[0][i] == 0:
                top_row = True
                break

        for i in range(1, ROWS):
            for j in range(0, COLS):
                if matrix[i][j] == 0:
                    matrix[0][j], matrix[i][0] = 0, 0
        
        for i in range(1, COLS):
            if matrix[0][i] == 0:
                for j in range(1, ROWS):
                    matrix[j][i] = 0
        
        for i in range(1, ROWS):
            if matrix[i][0] == 0:
                for j in range(1, COLS):
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(ROWS):
                matrix[i][0] = 0

        if top_row:
            for i in range(COLS):
                matrix[0][i] = 0
