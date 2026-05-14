class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.word_end = True

    def search(self, word: str) -> bool:
        word_last_index = len(word) - 1

        def node_search(node, letter_index):

            if word[letter_index] != ".":
                if word[letter_index] not in node.children:
                    return False
                node = node.children[word[letter_index]]

                if letter_index == word_last_index:
                    return node.word_end

                return node_search(node, letter_index + 1)

            for child in node.children:
                if letter_index == word_last_index:
                    return node.children[child].word_end

                if node_search(node.children[child], letter_index + 1):
                    return True
            
            return False

        return node_search(self.root, 0)
            

