class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        tracker = {}

        def string_check(indexs, indexp):
            if (indexs, indexp) in tracker:
                return tracker[(indexs, indexp)]

            if indexp >= len(p):
                return indexs >= len(s)

            match = indexs < len(s) and (p[indexp] == "." or s[indexs] == p[indexp])
            checkhash = indexp + 1 < len(p) and p[indexp + 1] == "*"
            
            if checkhash:
                tracker[(indexs, indexp)] = string_check(indexs, indexp + 2) or (match and string_check(indexs + 1, indexp))
                return tracker[(indexs, indexp)]

            if match:
                tracker[(indexs, indexp)] = string_check(indexs + 1, indexp + 1)
                return tracker[(indexs, indexp)]

            tracker[(indexs, indexp)] = False
            return tracker[(indexs, indexp)]

        return string_check(0, 0)