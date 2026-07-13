class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def check_safe(row, col):
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return

            if board[row][col] != 'O':
                return

            board[row][col] = '!'
            for direction in directions:
                check_safe(row + direction[0], col + direction[1])

        for i in range(ROWS):
            if board[i][0] == 'O':
                check_safe(i, 0)

            if board[i][COLS - 1] == 'O':
                check_safe(i, COLS - 1)

        for i in range(0, COLS):
            if board[0][i] == 'O':
                check_safe(0, i)

            if board[ROWS - 1][i] == 'O':
                check_safe(ROWS - 1, i)


        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "!":
                    board[i][j] = 'O'

                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        
