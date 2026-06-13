class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        s1_check = {}
        s2_check = {}

        for i in alphabets:
            s1_check[i] = 0
            s2_check[i] = 0

        for i in range(len(s1)):
            s1_check[s1[i]] += 1
            s2_check[s2[i]] += 1

        matches = 0
        for i in alphabets:
            if s2_check[i] == s1_check[i]:
                matches += 1
        
        if matches == 26:
            return True

        pleft = 0
        for i in range(len(s1), len(s2)):
            char = s2[i]
            s2_check[char] += 1

            if s2_check[char] == s1_check[char] + 1:
                matches -= 1
            elif s2_check[char] == s1_check[char]:
                matches += 1

            left_char = s2[pleft]
            s2_check[left_char] -= 1
            if s2_check[left_char] == s1_check[left_char] - 1:
                matches -= 1
            elif s2_check[left_char] == s1_check[left_char]:
                matches += 1

            if matches == 26:
                return True
            
            pleft += 1

        return False
