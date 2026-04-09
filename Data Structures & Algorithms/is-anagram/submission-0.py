class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = self.count_characters(s)
        t_counter = self.count_characters(t)

        return s_counter == t_counter

    def count_characters(self, string):

        character_counter = [0] * 26

        for character in string:
            character_counter[ord(character) - 97] += 1

        return character_counter
