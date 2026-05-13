class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])

        if len(word) > ROWS * COLS:
            return False

        def next_letter(i, j, letter_index):
            if letter_index == len(word):
                return True

            if not 0 <= i < ROWS or not 0 <= j < COLS or board[i][j] != word[letter_index] or board[i][j] == "#":
                return False
            
            board[i][j] = "#"
            x = next_letter(i - 1, j, letter_index + 1) or next_letter(i + 1, j, letter_index + 1) or next_letter(i, j + 1, letter_index + 1) or next_letter(i, j - 1, letter_index + 1)
            board[i][j] = word[letter_index]

            return x

        for i in range(ROWS):
            for j in range(COLS):
                if next_letter(i, j, 0):
                    return True
   
        return False