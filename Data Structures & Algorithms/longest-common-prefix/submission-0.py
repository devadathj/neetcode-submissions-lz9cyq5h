class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        output = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < min(len(output), len(strs[i])):
                if output[j] != strs[i][j]:
                    break
                j += 1

            output = output[:j] 

        return output