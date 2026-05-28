class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        s_len = len(s)

        self.output = ''
        self.output_len = 0

        def palin_check(l, r):
            while l >= 0 and r < s_len and s[l] == s[r]:

                if  r - l + 1 > self.output_len:
                    self.output_len = r - l + 1
                    self.output = s[l: r + 1]
                
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
