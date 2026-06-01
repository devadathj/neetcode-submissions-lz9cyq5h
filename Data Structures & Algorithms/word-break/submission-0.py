class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        s_len = len(s)

        checker = [False] * (s_len + 1)
        checker[s_len] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= s_len and s[i: i + len(w)] == w:
                    checker[i] = checker[i + len(w)]
                if checker[i]:
                    break

        return checker[0]