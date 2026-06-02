class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        check_map = {}
        t1_len, t2_len = len(text1), len(text2)

        def LCS(i1, i2):

            if (i1, i2) in check_map:
                return check_map[(i1, i2)]

            if i1 >= t1_len or i2 >= t2_len:
                return 0

            if text1[i1] == text2[i2]:
                check_map[(i1, i2)] = 1 + LCS(i1 + 1, i2 + 1)
            else:
                check_map[(i1, i2)] = max(LCS(i1, i2 + 1), LCS(i1 + 1, i2))

            return check_map[(i1, i2)]

        return LCS(0, 0)