class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        last_character = {}
        output = 0
        last_repeat_index = -1

        for i, character in enumerate(s):
            
            if character in last_character.keys():    
                last_repeat_index = max(last_character[character], last_repeat_index)

            last_character[character] = i
            output = max(output, i - last_repeat_index)
        
        return output
            
