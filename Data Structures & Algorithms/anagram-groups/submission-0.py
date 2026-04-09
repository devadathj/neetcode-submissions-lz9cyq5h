class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        character_count_map = list()
        output = list()

        for string in strs:

            string_map = self.count_characters(string)

            for i in range(len(character_count_map)):
                if string_map == character_count_map[i]:
                    output[i].append(string)
                    break
            else:
                character_count_map.append(string_map)
                output.append([string])

        return output

    def count_characters(self, string):

        count_map = [0] * 26

        for character in string:
            count_map[ord(character) - 97] += 1

        return count_map