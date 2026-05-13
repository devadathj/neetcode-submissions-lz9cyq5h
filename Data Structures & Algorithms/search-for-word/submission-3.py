class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])

        if len(word) > ROWS * COLS:
            return False
            
        if ROWS == 1:
            if ".".join(board[0]) == word:
                return True

        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        opposite_directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def next_letter(i, j, negate:[], letter_index):
            for k in range(len(directions)):
                if 0 <= i + directions[k][0] < ROWS and 0 <= j + directions[k][1] < COLS and directions[k] != negate:
                    if board[i + directions[k][0]][j + directions[k][1]] == word[letter_index]:
                        if letter_index == len(word) - 1:
                            return True
                        if next_letter(i + directions[k][0], j + directions[k][1], opposite_directions[k], letter_index + 1):
                            return True

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:

                    if len(word) > 1:
                        if next_letter(i, j, [], 1):
                            return True
                    else:
                        return True
        return False