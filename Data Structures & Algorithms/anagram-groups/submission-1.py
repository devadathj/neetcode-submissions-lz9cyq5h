from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        character_count_map = defaultdict(list)

        for string in strs:

            string_map = self.count_characters(string)

            character_count_map[tuple(string_map)].append(string)

        return list(character_count_map.values())

    def count_characters(self, string):

        count_map = [0] * 26

        for character in string:
            count_map[ord(character) - 97] += 1

        return count_map