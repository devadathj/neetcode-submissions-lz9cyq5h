class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_check = {}
        s2_check = {}

        for char in s1:
            s1_check[char] = s1_check.get(char, 0) + 1

        pleft = 0
        for i, char in enumerate(s2):
            if char in s1_check:
                s2_check[char] = s2_check.get(char, 0) + 1

                if s2_check[char] > s1_check[char]:
                    if s2[pleft] == char:
                        pleft += 1
                        s2_check[char] -= 1
                        
                if s1_check == s2_check:
                    return True
            else:
                s2_check = {}

        return False
