class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        tracker = {}

        def matcher(index1, index2):
            if index2 == len(word2):
                return len(word1) - index1
            if index1 == len(word1):
                return len(word2) - index2 
            
            if (index1, index2) in tracker:
                return tracker[(index1, index2)]

            if word1[index1] != word2[index2]:
                tracker[(index1, index2)] = 1 + min(matcher(index1, index2 + 1), matcher(index1 + 1, index2), matcher(index1 + 1, index2 + 1))
            else:
                tracker[(index1, index2)] = matcher(index1 + 1, index2 + 1)

            return tracker[(index1, index2)]

        return matcher(0, 0)