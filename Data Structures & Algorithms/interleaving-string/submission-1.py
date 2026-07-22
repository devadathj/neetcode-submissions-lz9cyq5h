class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    
        if len(s1) + len(s2) != len(s3):
            return False

        tracker = {}

        def weaver(i, j):

            if i == len(s1) and j == len(s2):
                return True

            if (i, j) in tracker:
                return tracker[(i, j)]

            tracker[(i, j)] = False
            if i < len(s1) and not tracker[(i, j)] and s1[i] == s3[i + j]:
                tracker[(i, j)] = weaver(i + 1, j)
            
            if j < len(s2) and not tracker[(i, j)] and s2[j] == s3[i + j]:
                tracker[(i, j)] = weaver(i, j + 1)

            return tracker[(i, j)]

        return weaver(0, 0)
