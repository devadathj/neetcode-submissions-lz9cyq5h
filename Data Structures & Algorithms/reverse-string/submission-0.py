class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s) - 1
        i = 0
        while i < len(s) / 2:
            s[i], s[s_len - i] = s[s_len - i], s[i]
            i += 1
            
        return s