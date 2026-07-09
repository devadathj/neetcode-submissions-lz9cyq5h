class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        output = []
        arr = []

        def palindrome_check(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        def make_substring(i):
            if i >= len(s):
                output.append(arr.copy())
                return

            for j in range(i, len(s)):
                if palindrome_check(i, j):
                    arr.append(s[i: j + 1])
                    make_substring(j + 1)
                    arr.pop()

        make_substring(0)
        return output
        
