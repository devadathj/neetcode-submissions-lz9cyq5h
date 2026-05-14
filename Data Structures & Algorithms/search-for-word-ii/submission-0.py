class TrieNode():
    def __init__(self):
        self.children = {}
        self.word_index = -1

    def addWord(self, word: str, index: int) -> None:
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.word_index = index

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        output = []

        root = TrieNode()
        for index, word in enumerate(words):
            root.addWord(word, index)

        ROWS, COLS = len(board), len(board[0])
                
        def word_search(row, col, node):
            if not 0 <= row < ROWS or not 0 <= col < COLS or board[row][col] == "#":
                return 

            if board[row][col] not in node.children:
                return 
            
            current_char = board[row][col]

            if node.children[current_char].word_index != -1:
                output.append(words[node.children[current_char].word_index])
                node.children[current_char].word_index = -1

            board[row][col] = "#"

            word_search(row + 1, col, node.children[current_char])
            word_search(row - 1, col, node.children[current_char])
            word_search(row, col + 1, node.children[current_char])
            word_search(row, col - 1, node.children[current_char])

            board[row][col] = current_char

            return 

        for row in range(ROWS):
            for col in range(COLS):
                word_search(row, col, root)

        return output

        