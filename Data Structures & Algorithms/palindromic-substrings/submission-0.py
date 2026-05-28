class Solution:
    def countSubstrings(self, s: str) -> int:
        
        s_len = len(s)
        self.output= 0

        def palin_check(l, r):
            while l >= 0 and r < s_len and s[l] == s[r]:
                self.output += 1
                l -= 1
                r += 1

        for i in range(s_len):
            l = i
            r = i
            palin_check(l, r)
            
            l = i
            r = i + 1
            palin_check(l, r)

        return self.output
