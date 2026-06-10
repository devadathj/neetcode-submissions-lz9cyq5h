class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        box_directions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1), (0, 0), (0, 1),
                          (1, -1), (1, 0), (1, 1)]

        def check_box(i, k):

            check_set = set()

            for j in box_directions:
                if board[i + j[0]][k + j[1]] != ".":
                    if board[i + j[0]][k + j[1]] in check_set:
                        return False
                    check_set.add(board[i + j[0]][k + j[1]])

            return True

        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])

            col_set = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])

            if i in {1, 4, 7}:
                if not check_box(i, 1) or not check_box(i, 4) or not check_box(i, 7):
                    return False
        
        return True
            

