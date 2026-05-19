class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        word_order = {i : set() for word in words for i in word }

        for i in range(len(words) - 1):

            min_len = min(len(words[i]), len(words[i + 1]))

            if len(words[i]) > len(words[i + 1]) and words[i][:min_len] == words[i + 1]:
                return ""

            for j in range(min_len):
                if words[i][j] != words[i + 1][j]:
                    word_order[words[i][j]].add(words[i + 1][j])
                    break

        output = []
        output_letters = set()

        def check_order(letter, visited):
            if letter not in word_order:
                output.append(letter)
                output_letters.add(letter)
                return True

            if letter in output_letters:
                return True

            if letter in visited:
                return False

            visited.add(letter)
            for i in word_order[letter]:
                if not check_order(i, visited):
                    return False

            visited.remove(letter)
            output.append(letter)
            output_letters.add(letter)
            return True

        for i in word_order.keys():
            if not check_order(i, set()):
                return ""

        return "".join(reversed(output))
