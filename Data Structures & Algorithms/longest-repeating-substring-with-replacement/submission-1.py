class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        character_count = {}
        output = 0

        left = 0
        for right in range(len(s)):
            character_count[s[right]] = character_count.get(s[right], 0) + 1

            if right - left + 1 - max(character_count.values()) <= k:
                output = max(output, right - left + 1)
            else:
                character_count[s[left]] -= 1
                left += 1

        return output

